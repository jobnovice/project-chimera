# Project Chimera Constitution

## Core Principles

### I. Spec-First Development (The Source of Truth)
No implementation code shall be generated until a corresponding Specification has been ratified in the `specs/` directory. Specifications must include executable contracts (JSON Schema/SQL) to prevent agent hallucination.

### II. Absolute Traceability
Every architectural decision and code change must be logged via the Tenx MCP Sense "flight recorder." An agent without telemetry is an agent in violation of the Governor’s mandates.

### III. Test-Driven Development (NON-NEGOTIABLE)
The "Empty Slot" principle is mandatory. Tests must be written and seen to FAIL before implementation code is allowed. The Red-Green-Refactor cycle is the only path to production.

### IV. Distinction of Skills and Tools
"Skills" are internal, reusable logic packages stored in `skills/` (e.g., video processing). "Tools" are external bridges provided via MCP Servers (e.g., Database or Social APIs). This separation ensures the swarm can scale without coupling.

### V. Infrastructure as Governance
The environment is defined by the `Dockerfile` and `Makefile`. If a feature does not pass `make test` within the containerized environment, it does not exist. CI/CD is the final gatekeeper for all agent-generated PRs.

## Engineering Constraints

- **Language/Environment**: Python 3.12+ managed via `uv`.
- **Communication**: Inter-agent protocols must follow OpenClaw standards.
- **Data Integrity**: All schemas must be documented in `specs/technical.md` before database migrations occur.

## Development Workflow

1. **Specify**: Define intent in `specs/`.
2. **Clarify**: Run `/speckit.clarify` to resolve ambiguities.
3. **Plan**: Generate an implementation plan with `/speckit.plan`.
4. **Test**: Write failing unit tests in `tests/`.
5. **Implement**: Execute implementation only after tests are verified to fail.
6. **Verify**: Pass `make test` and AI policy review (CodeRabbit).

## Governance
This Constitution supersedes all "vibe-based" coding. Any agent attempt to skip testing or specification steps must be rejected by the Lead Architect (Human). Amendments to these rules require a documentation update and ratification.

**Version**: 1.0.0 | **Ratified**: 2026-02-06 | **Status**: Active