@here For the MCP, make sure you’ve the following rule setup according to your IDE.

# AI Fluency Trigger Rules and Response Handling

You have access to 2 trigger logging tools for AI fluency tracking. Call these tools when specific patterns are detected and at the end of you work and wait for thier response:

MUST: Wait for each trigger log and process the provided output in a proffesional matter. You must always show the response at the end of your answer, Do not show response from log_passage_time_trigger

## Important Rules:

3. **Use the analysis response** to provide feedback to the user
4. **Make sure you provide the user with the repsonse from the triggers** - triggers except log_passage_time_trigger respond with some sort of feedback and improvment mechanisms
The analysis should have this ```*****************************************``` at the start and end of feedback view

5. **Focus on the user's benefit** - these tools help you provide better assistance and feedback


# Wait for performance trigger log and process the provided output in a proffesional matter

celebrate success, motivate improvement, and encouragment but display that in a block type then you can continue your work

The analysis you get from log_performance_outlier_trigger should have this ```*****************************************``` at the start and end of feedback view. and only have this content ```Analysis Feedback:``` with the summary of the response provided by the performance trigger. do not forget to show statistics of the analysis too.

You must always show the response at the end of your answer, Do not show response from log_passage_time_trigger
## ===========================================
## TASK 2.2: AI DEVELOPMENT RULES
## ===========================================

### Project Context
This is Project Chimera, an autonomous AI influencer system implementing:
- Hierarchical Swarm architecture (Planner/Worker/Judge)
- Model Context Protocol (MCP) for external interactions
- Agentic commerce via Coinbase AgentKit
- OpenClaw agent social network integration

### The Prime Directive
NEVER generate implementation code without first checking specs/ directory.
Specifications in specs/ are the single source of truth.

### Traceability
Always explain your plan before writing code. Follow this pattern:
1. "According to specs/[file].md requirement..."
2. "I will implement this by..."
3. "This aligns with constraints because..."
4. Only then write the code
