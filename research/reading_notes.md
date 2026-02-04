# Research Notes - Project Chimera

## Key Insights from Reading Materials

### The Trillion Dollar AI Code Stack (a16z)
- Emphasizes agentic workflows: Plan-Code-Review cycle
- Spec-driven development (SDD) to prevent AI hallucinations
- AI-native practices: natural language specs, .cursor/rules for LLMs
- Tools for AI collaboration: background agents, AI QA, code sandboxes
- Semantic version control for AI-generated code
- Massive productivity gains for developers

### OpenClaw & MoltBook
- **OpenClaw**: Viral open-source AI assistant (100k+ GitHub stars)
- **MoltBook**: Social network for AI agents
- Agents interact via "Submolts" and skills
- Enables self-organization around topics (automation, etc.)
- Evolution of DIY AI agents and bot social platforms
- Skill-based interactions for machine-readable communication

## Project Chimera and Agent Social Networks

Project Chimera fits into the OpenClaw ecosystem as an autonomous influencer agent that:
1. **Publishes content, status, and availability** to Moltbook-like networks
2. **Participates in "Submolts"** for trend discovery and collaboration
3. **Fetches viral topics** from agent discussions
4. **Co-generates content** with peer AIs
5. **Shares engagement metrics** with the network

This turns solitary influencers into networked entities, leveraging OpenClaw's skill-based interactions for machine-readable posts and reducing latency in trend research.

## Social Protocols for Agents

Chimera agents need protocols beyond human APIs:

1. **Communication Protocol**: JSON-RPC over WebSockets for real-time status pings
   - Example: `{"availability": "active", "skills": ["trend_fetch", "content_gen"]}`

2. **Data Exchange Protocol**: Semantic feeds in YAML for trend sharing
   - Example: `submolt: viral_challenges, payload: {trend_id: 123, virality_score: 0.9}`

3. **Skill Marketplace Protocol**: Modular capability exchange
   - Example: `download_video` skill contract: input `{url}`, output `{metadata}`

4. **Security Protocol**: Signed prompts to prevent injection attacks
5. **Human Oversight Protocol**: Content approval workflows

These protocols ensure interoperability in swarms, with MCP traceability logging all interactions.
