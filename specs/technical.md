# Project Chimera - Technical Specifications (Placeholder)

## API Contracts
*To be defined based on functional requirements*

## Database Schema  
*To be defined - will include:*
- Video metadata tables
- Agent persona storage  
- Transaction logs
- Review queue

## MCP Tool Definitions
*Standard MCP tool schemas for:*
- Social media posting
- Content generation
- Financial transactions
- Memory management

## OpenClaw Protocols
*Inter-agent communication standards*


---

## Database DDL (Postgres)

-- video_metadata: stores canonical metadata about source videos
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS video_metadata (
	id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
	external_id TEXT UNIQUE, -- source platform id
	title TEXT NOT NULL,
	description TEXT,
	uploader_id UUID,
	duration_seconds INTEGER,
	tags TEXT[],
	metadata JSONB, -- freeform parsed metadata (codec, resolution, thumbnails)
	status TEXT NOT NULL DEFAULT 'ingested', -- ingested, processed, published, blocked
	confidence NUMERIC(4,3) DEFAULT 0.0, -- aggregate confidence 0.000-1.000
	created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
	updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_video_uploader ON video_metadata (uploader_id);
CREATE INDEX IF NOT EXISTS idx_video_created_at ON video_metadata (created_at DESC);
CREATE INDEX IF NOT EXISTS idx_video_tags_gin ON video_metadata USING gin (tags);
CREATE INDEX IF NOT EXISTS idx_video_metadata_gin ON video_metadata USING gin (metadata jsonb_path_ops);

-- agent_tasks: queue of tasks assigned to agents (Worker/Judge/Planner)
CREATE TABLE IF NOT EXISTS agent_tasks (
	id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
	task_type TEXT NOT NULL, -- e.g., 'analyze_video', 'generate_caption', 'human_review'
	agent_id TEXT, -- logical agent name or persona id
	payload JSONB NOT NULL, -- task-specific inputs
	priority SMALLINT NOT NULL DEFAULT 50, -- 0 (highest) - 100 (lowest)
	status TEXT NOT NULL DEFAULT 'pending', -- pending, running, failed, succeeded, cancelled
	attempts SMALLINT NOT NULL DEFAULT 0,
	last_attempt_at TIMESTAMPTZ,
	result JSONB,
	confidence NUMERIC(4,3) DEFAULT 0.0,
	scheduled_for TIMESTAMPTZ,
	created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
	updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_tasks_status_priority ON agent_tasks (status, priority);
CREATE INDEX IF NOT EXISTS idx_tasks_agentid ON agent_tasks (agent_id);
CREATE INDEX IF NOT EXISTS idx_tasks_scheduled ON agent_tasks (scheduled_for);

-- review_queue: human review tasks, decisions and provenance
CREATE TABLE IF NOT EXISTS review_queue (
	id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
	video_id UUID REFERENCES video_metadata(id) ON DELETE CASCADE,
	task_id UUID REFERENCES agent_tasks(id) ON DELETE SET NULL,
	reviewer_id UUID, -- human reviewer identity
	requested_by TEXT, -- agent or system that requested review
	requested_at TIMESTAMPTZ NOT NULL DEFAULT now(),
	assigned_at TIMESTAMPTZ,
	completed_at TIMESTAMPTZ,
	decision TEXT, -- approved | rejected | needs_more_info
	notes TEXT,
	human_confidence NUMERIC(4,3),
	evidence JSONB, -- supporting artifacts (timestamps, clips, comments)
	created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
	updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_review_video ON review_queue (video_id);
CREATE INDEX IF NOT EXISTS idx_review_assigned ON review_queue (assigned_at);

---

## JSON Schemas

### Agent Task Protocol (JSON Schema)

```json
{
	"$schema": "http://json-schema.org/draft-07/schema#",
	"title": "Agent Task",
	"type": "object",
	"required": ["id","task_type","payload","created_at"],
	"properties": {
		"id": {"type":"string","format":"uuid"},
		"task_type": {"type":"string","description":"Logical task name e.g. analyze_video"},
		"agent_id": {"type":"string","description":"Assigned agent persona id or name"},
		"payload": {"type":"object","description":"Task-specific input; validated per task_type"},
		"priority": {"type":"integer","minimum":0,"maximum":100},
		"status": {"type":"string","enum":["pending","running","failed","succeeded","cancelled"]},
		"attempts": {"type":"integer","minimum":0},
		"scheduled_for": {"type":"string","format":"date-time"},
		"created_at": {"type":"string","format":"date-time"},
		"updated_at": {"type":"string","format":"date-time"}
	},
	"additionalProperties": true
}
```

Notes:
- Task-specific schemas may be registered keyed by `task_type`. Consumers MUST validate `payload` against the corresponding `task_type` schema before executing.

---

### OpenClaw Status Schema (confidence gating: human review between 0.7 and 0.9)

This schema captures automated scoring and routing decisions. The system implements the following gating rule (OpenClaw):
- If `automated_confidence >= 0.90` -> `action`: "auto_approve"
- If `automated_confidence < 0.70` -> `action`: "auto_reject"
- If `0.70 <= automated_confidence < 0.90` -> `action`: "human_review_required"

```json
{
	"$schema": "http://json-schema.org/draft-07/schema#",
	"title": "OpenClawStatus",
	"type": "object",
	"required": ["video_id","automated_confidence","action","evaluated_at"],
	"properties": {
		"video_id": {"type":"string","format":"uuid"},
		"automated_confidence": {"type":"number","minimum":0,"maximum":1},
		"action": {"type":"string","enum":["auto_approve","auto_reject","human_review_required"]},
		"evaluated_by": {"type":"string","description":"model or pipeline id"},
		"evaluated_at": {"type":"string","format":"date-time"},
		"reason": {"type":"string"},
		"provenance": {"type":"object"},
		"human_review": {
			"type":"object",
			"properties": {
				"review_id": {"type":"string","format":"uuid"},
				"reviewer_id": {"type":"string"},
				"decision": {"type":"string","enum":["approved","rejected","needs_more_info"]},
				"human_confidence": {"type":"number","minimum":0,"maximum":1},
				"notes": {"type":"string"},
				"completed_at": {"type":"string","format":"date-time"}
			}
		}
	},
	"additionalProperties": false
}
```

---

## MCP Tool Definitions

The following outlines the MCP tool surface for core agent roles: `Judge` and `Worker`. Tools are described at a high level; implementers should map these into the runtime MCP tool registry (name, JSON input schema, JSON output schema, sync/async semantics).

### Worker Agent Tools

- `worker.execute_task`
	- Description: Execute an `Agent Task` (e.g., analyze media, generate caption, post content). Intended to be idempotent for retry safety.
	- Input (JSON): conforms to `Agent Task` protocol schema (see above). Tools SHOULD validate `payload` per `task_type`.
	- Output (JSON): `{ "task_id": "<uuid>", "status": "succeeded|failed", "result": {...}, "confidence": 0.0-1.0 }`
	- Semantics: asynchronous execution allowed; caller can poll task status via `agent_tasks` table or via `worker.query_task_status` tool.

- `worker.query_task_status`
	- Input: `{ "task_id": "<uuid>" }`
	- Output: `{ "task_id": "<uuid>", "status": "pending|running|failed|succeeded|cancelled", "result": {...}, "confidence": number }

### Judge Agent Tools

- `judge.evaluate_review`
	- Description: Evaluate outputs (automated or human) and produce a final disposition and confidence. The Judge consolidates signals (automated model, worker result, human review) and writes a review record.
	- Input: `{ "video_id": "<uuid>", "evidence": {...}, "automated_confidence": number, "worker_result": {...} }`
	- Output: `{ "video_id":"<uuid>", "final_decision": "approved|rejected|needs_more_info", "final_confidence": number, "reason": "string" }
	- Semantics: Must record a traceable provenance object; for borderline automated_confidence (0.7-0.9) Judge SHOULD require and incorporate human review before finalizing.

- `judge.request_human_review`
	- Input: `{ "video_id": "<uuid>", "reason": "string", "context": {...} }`
	- Output: `{ "review_id": "<uuid>", "assigned": true, "queue_entry": {...} }

---

## Notes on Alignment with Architecture

- Storage: schemas and DDL are Postgres-first (JSONB for opaque payloads). Redis is assumed for transient worker queues and fast locking, while Postgres stores authoritative state.
- Confidence Scoring: `confidence` fields are numeric(4,3) to explicitly encode 0.000-1.000 values and allow consistent gating logic (see OpenClaw thresholds above).
- TDD & Spec-First: Any implementation MUST add unit/integration tests that first assert schema validity and gating logic (automated_confidence thresholds) prior to feature code.

---

## Implementation Requirements

The following implementation files are required by the system and must be present in the repository for the feature to be considered implemented:

- skills/trend_fetcher.py
- skills/skills_interface.py
- tests/test_trend_fetcher.py
- tests/test_skills_interface.py

Implementers MUST ensure these modules conform to the `Agent Task` protocol and include tests that validate against the JSON schemas and Postgres DDL defined above.



