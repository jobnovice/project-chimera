# Project Chimera: Autonomous Influencer Network

[![Spec-Driven Development](https://img.shields.io/badge/Methodology-Spec--Driven-blueviolet)](https://github.com/features/copilot)
[![Governance: Ratified](https://img.shields.io/badge/Governance-Ratified-green)](#governance)
[![Environment: uv](https://img.shields.io/badge/Environment-uv-blue)](https://github.com/astral-sh/uv)

Project Chimera is a robust engineering framework for building Autonomous AI Influencers. Unlike fragile "prompt-engineered" prototypes, Chimera uses **Spec-Driven Development (SDD)** to ensure that AI agents operate within strict architectural boundaries.

---

## 🏗 Architecture & Governance

### The "Governor" Philosophy
This repository is governed by a **Constitution** (located in `.specify/memory/constitution.md`). All code must align with the ratified `specs/` before implementation. 

* **Pattern**: Hierarchical Swarm (Planner/Worker/Judge).
* **Traceability**: Full telemetry captured via **Tenx MCP Sense**.
* **Validation**: Automated `spec_check.py` auditor ensures code-to-spec alignment.



---

## 🚀 Quick Start

### Prerequisites
* [uv](https://github.com/astral-sh/uv) installed (Python package manager).
* Docker (for production parity).
* Tenx MCP Sense (connected for flight recording).

### Installation & Setup
```bash
# Setup the environment and install dependencies
make setup


Development Workflow (TDD)
We follow a strict Red-Green-Refactor cycle enforced by the Makefile:
# 1. Verify Specification Alignment
make spec-check

# 2. Run Local Test Suite (TDD Proof)
make test-local
📂 Project Structure
specs/: The "Source of Truth." Contains functional, technical, and API contracts.

skills/: Modular, independently testable agent capabilities (Trend Research, Content Gen).

tests/: TDD-first test suite validating against JSON schemas.

research/: Architecture strategies and domain deep-dives.

.specify/: GitHub Spec Kit governance toolkit and project constitution.

.

🛠 Tech Stack
Language: Python 3.12+ (uv)

Database: PostgreSQL (Metadata), Redis (Task Queue)

Orchestration: Docker & GitHub Actions

Protocol: Model Context Protocol (MCP) & OpenClaw
OpenClaw

📜 Governance Status
Day 1 (Strategist): Complete ✅

Day 2 (Architect): Complete ✅

Day 3 (Governor): Complete ✅

Lead Architect: [Eyob Kebede/GitHub: https://github.com/jobnovice]