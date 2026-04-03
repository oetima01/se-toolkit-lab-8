# Lab 8 — Report

Paste your checkpoint evidence below. Add screenshots as image files in the repo and reference them with `![description](path)`.

## Task 1A — Bare agent

**Q: "What is the agentic loop?"**

The agentic loop is the continuous cycle an AI agent uses to solve problems autonomously. It consists of four main phases:

1. **Perceive:** The agent gathers information from the user, files, tools, or environment.
2. **Reason:** It analyzes the context, plans the next steps, and decides which tools to use.
3. **Act:** It executes the chosen actions (e.g., running a script, writing a file, making an API call).
4. **Observe:** It reviews the results of those actions to determine if the goal is met or if further steps are needed.

This loop repeats until the task is successfully completed or an error occurs that requires intervention.

**Q: "What labs are available in our LMS?"** (no MCP tools — bare agent)

Based on search through the codebase, documentation, and test data:

| Lab ID | Where Referenced |
|--------|-----------------|
| lab-01 | Analytics API, lab plan docs |
| lab-02 | Codebase references |
| lab-03 | Test data |
| lab-04 | Analytics API, deployment docs, test data |

The LMS MCP tools aren't available in this session — they require the `NANOBOT_LMS_BACKEND_URL` and `NANOBOT_LMS_API_KEY` environment variables. The agent inspects local repo files and answers from documentation instead of the live LMS.

## Task 1B — Agent with LMS tools

**Q: "What labs are available?"** (with MCP tools connected)

MCP server `lms` connected — 9 tools registered: `lms_health`, `lms_labs`, `lms_learners`, `lms_pass_rates`, `lms_timeline`, `lms_groups`, `lms_top_learners`, `lms_completion_rate`, `lms_sync_pipeline`.

The agent called `mcp_lms_lms_labs({})` and returned:

| # | Lab |
|---|-----|
| 1 | Lab 01 – Products, Architecture & Roles |
| 2 | Lab 02 — Run, Fix, and Deploy a Backend Service |
| 3 | Lab 03 — Backend API: Explore, Debug, Implement, Deploy |
| 4 | Lab 04 — Testing, Front-end, and AI Agents |
| 5 | Lab 05 — Data Pipeline and Analytics Dashboard |
| 6 | Lab 06 — Build Your Own Agent |
| 7 | Lab 07 — Build a Client with an AI Coding Agent |
| 8 | lab-08 |

**Q: "Is the LMS backend healthy?"**

The agent called `mcp_lms_lms_health({})` and responded:

> Yes, the LMS backend is healthy! It's currently managing 56 items.

## Task 1C — Skill prompt

**Q: "Show me the scores"** (without specifying a lab — skill prompt guides behavior)

The LMS skill prompt guided the agent to query live data. Since only Lab 01 has interaction data so far, the agent returned:

### Lab 01 – Products, Architecture & Roles

| Task | Avg Score | Attempts | Students |
|------|-----------|----------|----------|
| Lab setup | 97.2 | 139 | 115 |
| Task 0: Practice the Git workflow | 65.2 | 214 | 98 |
| Task 1: Product & architecture description | 59.4 | 90 | 59 |
| Task 2: Roles and skills mapping | 53.9 | 42 | 33 |
| Optional: Resolve a merge conflict | 41.7 | 6 | 5 |
| Optional: Create a release | 50.0 | 2 | 2 |
| Optional: Add a CI check | 25.0 | 4 | 3 |
| Optional: Plan skill development | 0.0 | 1 | 1 |

**Completion:** 0 out of 115 students have passed all required tasks (score ≥ 50 on all 4 required tasks).

**Top Learners:**

| Student | Group | Avg Score | Attempts |
|---------|-------|-----------|----------|
| 440fac56 | B25-CSE-02 | 100.0 | 1 |
| 5f77b9dc | B25-DSAI-01 | 100.0 | 2 |
| b4ba2a84 | B25-CSE-05 | 100.0 | 2 |

Note: Only Lab 01 has interaction data so far. Labs 02–08 exist in the catalog but have no submissions yet.

## Task 2A — Deployed agent

<!-- Paste a short nanobot startup log excerpt showing the gateway started inside Docker -->

## Task 2B — Web client

<!-- Screenshot of a conversation with the agent in the Flutter web app -->

## Task 3A — Structured logging

<!-- Paste happy-path and error-path log excerpts, VictoriaLogs query screenshot -->

## Task 3B — Traces

<!-- Screenshots: healthy trace span hierarchy, error trace -->

## Task 3C — Observability MCP tools

<!-- Paste agent responses to "any errors in the last hour?" under normal and failure conditions -->

## Task 4A — Multi-step investigation

<!-- Paste the agent's response to "What went wrong?" showing chained log + trace investigation -->

## Task 4B — Proactive health check

<!-- Screenshot or transcript of the proactive health report that appears in the Flutter chat -->

## Task 4C — Bug fix and recovery

<!-- 1. Root cause identified
     2. Code fix (diff or description)
     3. Post-fix response to "What went wrong?" showing the real underlying failure
     4. Healthy follow-up report or transcript after recovery -->
