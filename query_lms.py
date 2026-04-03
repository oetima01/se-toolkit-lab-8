#!/usr/bin/env python3
"""Query LMS for labs and scores."""
import asyncio
import sys
import os

# Add MCP source to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "mcp", "mcp-lms", "src"))

from mcp_lms.client import LMSClient

BASE_URL = os.environ.get("NANOBOT_LMS_BACKEND_URL", "http://127.0.0.1:42001")
API_KEY = os.environ.get("NANOBOT_LMS_API_KEY", "abcd")

async def main():
    async with LMSClient(base_url=BASE_URL, api_key=API_KEY) as client:
        # Get labs
        labs = await client.get_labs()
        print("=== Available Labs ===")
        for lab in labs:
            print(f"  {lab.id}: {lab.title}")
        
        print()
        
        # Get scores/pass rates for each lab
        for lab in labs:
            lab_id = str(lab.id) if lab.id else ""
            print(f"=== {lab_id}: {lab.title} ===")
            try:
                pass_rates = await client.get_pass_rates(lab_id)
                for pr in pass_rates:
                    print(f"  Task: {pr.task}, Avg Score: {pr.avg_score:.1f}%, Attempts: {pr.attempts}")
                
                completion = await client.get_completion_rate(lab_id)
                pct = completion.completion_rate * 100 if completion.completion_rate <= 1 else completion.passed/max(completion.total,1)*100
                print(f"  Completion: {completion.passed}/{completion.total} ({pct:.1f}%)")
            except Exception as e:
                print(f"  Error: {e}")
            print()

asyncio.run(main())
