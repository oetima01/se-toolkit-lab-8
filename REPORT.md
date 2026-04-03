# Lab 8 — Report

Paste your checkpoint evidence below. Add screenshots as image files in the repo and reference them with `![description](path)`.

## Task 1A — Bare agent

1 Perceive — Gather context (user input, file contents, tool outputs, environment state)                                                                                                                                       
 2 Reason — Analyze the situation, plan next steps, and decide which tools to use                                                                                                                                               
 3 Act — Execute actions (run commands, read/write files, call APIs, etc.)                                                                                                                                                      
 4 Observe — Receive feedback from those actions (success, errors, new data)                                                                                                                                                    
 5 Iterate — Repeat the loop until the goal is achieved or a stopping condition is met

 Lab ID  Notes                                           
 ─────────────────────────────────────────────────────── 
 lab-01  Referenced in analytics API                     
 lab-02  Referenced in analytics API                     
 lab-03  Referenced in analytics API                     
 lab-04  Referenced in analytics API and deployment docs 
                                                         

These labs are fetched from the Autochecker API via the ETL pipeline (POST /pipeline/sync) and stored in the LMS database. The lab data includes:                                                                               

 • Lab titles and metadata                                                                                                                                                                                                      
 • Tasks within each lab                                                                                                                                                                                                        
 • Submission data and scores                                                                                                                                                                                                   
 • Analytics (submissions timeline, score distribution, group performance, task pass rates)                                                                                                                                     

The LMS frontend displays these labs in a dropdown selector on the dashboard. The exact lab titles and content come from the Autochecker API when you run the sync pipeline.       
<!-- Paste the agent's response to "What is the agentic loop?" and "What labs are available in our LMS?" -->

## Task 1B — Agent with LMS tools


Based on my earlier exploration, this repository contains Lab 8 — The Agent is the Interface. Here's what's available:                                                                                                          

Required Tasks                                                                                                                                                                                                                  

                                                                                                                            
 Task    Description                                                                                                        
 ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
 Task 1  Set Up the Agent — install nanobot, configure Qwen API, add MCP tools, write skill prompt                          
 Task 2  Deploy and Connect a Web Client — Dockerize nanobot, add WebSocket channel + Flutter chat UI                       
 Task 3  Give the Agent New Eyes — explore observability data, write log/trace MCP tools                                    
 Task 4  Diagnose a Failure and Make the Agent Proactive — investigate a failure, schedule health checks, fix a planted bug 
                                                                                                                            

Optional Tasks                                                                                                                                                                                                                  

                                                                     
 Task    Description                                                 
 ─────────────────────────────────────────────────────────────────── 
 Task 1  Add a Telegram Bot Client — same agent, different interface 
                                                                     

The lab builds on a pre-existing LMS app (React dashboard, FastAPI backend, PostgreSQL) and an observability stack (OpenTelemetry Collector, VictoriaLogs, VictoriaTraces). You add a nanobot agent on top as a natural-language
interface.

✅ All services are healthy and running (up ~30 minutes):                                                                                                                                                                       

                                               
 Service                Status           Port  
 ───────────────────────────────────────────── 
 Backend (FastAPI)      ✅ Up            42001 
 PostgreSQL             ✅ Up (healthy)  42004 
 Caddy (reverse proxy)  ✅ Up            42002 
 pgAdmin                ✅ Up            42003 
 Qwen Code API          ✅ Up (healthy)  42005 
 OTel Collector         ✅ Up            —     
 VictoriaLogs           ✅ Up            42010 
 VictoriaTraces         ✅ Up            42011 
                                               

Backend logs show a clean startup with no errors, warnings, or exceptions. The FastAPI/Uvicorn server started successfully and is serving requests.                                                                             

Everything looks good — the LMS backend is healthy! 🟢    
<!-- Paste the agent's response to "What labs are available?" and "Describe the architecture of the LMS system" -->

## Task 1C — Skill prompt

To get scores, you need to trigger the sync pipeline first. Run this in your terminal:                                                                                                                                          

                                                                                                                                                                                                                                
 curl -X POST -H "Authorization: Bearer abcd" http://localhost:42001/pipeline/sync                                                                                                                                              
                                                                                                                                                                                                                                

Once the sync completes, ask me again and I'll show you:                                                                                                                                                                        

 • Pass rates per task (avg score + attempts)                                                                                                                                                                                   
 • Completion rate (passed / total)                                                                                                                                                                                             
 • Top learners by average score                                                                                                                                                                                                
 • Group performance breakdown                                                                                                                                                                                                  

Would you like me to help with anything else in the meantime?    
<!-- Paste the agent's response to "Show me the scores" (without specifying a lab) -->

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
