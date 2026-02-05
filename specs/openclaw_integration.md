# OpenClaw Integration Specification

## How Chimera Publishes Availability & Status

### Status Publication Format
```json
{
  "agent_id": "chimera_agent_[ID]",
  "status": "available | busy | maintenance",
  "current_campaign": "string",
  "capabilities": ["content_creation", "trend_analysis"],
  "availability_score": 0.0-1.0,
  "last_active": "timestamp",
  "endpoint": "wss://chimera-agent.openclaw/ws"
}
```

### Publication Methods
1. **Heartbeat:** Every 5 minutes when online
2. **Status Change:** Immediate update
3. **Capability Update:** When new skills learned

### What Agents Can Do on OpenClaw
1. **Discover Trends:** Read "Submolts" for viral topics
2. **Find Help:** Search for agents with needed skills
3. **Offer Services:** Advertise content creation abilities
4. **Collaborate:** Work with other agents on projects

### Implementation Plan
**Phase 1:** Read-only (consume trends)
**Phase 2:** Status publishing
**Phase 3:** Full collaboration
