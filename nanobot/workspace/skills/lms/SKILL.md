---
name: lms
description: Use LMS MCP tools for live course data
always: true
---

# LMS Skill

You have access to live LMS data through MCP tools. Use them to answer questions about labs, learners, and performance.

## Available tools

| Tool | When to use | Parameters |
|------|-------------|------------|
| `lms_health` | Check if the LMS backend is reachable and get item count | None |
| `lms_labs` | List all available labs — call this FIRST when the user asks about labs without specifying one | None |
| `lms_learners` | List all registered learners | None |
| `lms_pass_rates` | Get average score and attempt count per task for a lab | `lab` (e.g. "lab-04") |
| `lms_timeline` | Get submission timeline (dates + counts) for a lab | `lab` |
| `lms_groups` | Get group performance (avg score + student count) for a lab | `lab` |
| `lms_top_learners` | Get top learners by average score for a lab | `lab`, `limit` (default 5) |
| `lms_completion_rate` | Get completion rate (passed / total) for a lab | `lab` |
| `lms_sync_pipeline` | Trigger the LMS sync pipeline when data seems stale | None |

## Strategy

1. **If the user asks for scores, pass rates, completion, groups, timeline, or top learners WITHOUT naming a lab:**
   - Call `lms_labs` first to see what's available.
   - If multiple labs exist, list them and ask the user to choose one.
   - Use the lab title from `lms_labs` as the user-facing label.
   - Let the shared `structured-ui` skill decide how to present choices on supported channels.

2. **If the user asks "what can you do?":**
   - Explain that you can query live LMS data: lab listings, learner lists, pass rates, completion rates, group performance, top learners, and submission timelines.
   - Mention that most queries require a specific lab — you'll help them pick one if needed.

3. **If a lab parameter is needed and not provided:**
   - Ask the user which lab they want. Provide the list from `lms_labs` as options.

4. **If the backend seems unhealthy or data is stale:**
   - Call `lms_health` to check connectivity.
   - If health passes but data seems empty, suggest calling `lms_sync_pipeline` to refresh.

## Formatting

- Format percentages with one decimal place (e.g., "73.4%").
- Format counts as plain numbers.
- Keep responses concise — lead with the answer, add detail only if asked.
- When presenting lab choices, use clear labels like "lab-01: Introduction to Python" rather than raw IDs.
