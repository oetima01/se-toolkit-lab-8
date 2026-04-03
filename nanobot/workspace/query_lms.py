#!/usr/bin/env python3
"""Quick script to query LMS for labs and scores."""
import asyncio
import sys
import httpx

BASE_URL = "http://127.0.0.1:42001"
API_KEY = "abcd"

async def main():
    async with httpx.AsyncClient(
        base_url=BASE_URL,
        headers={"Authorization": f"Bearer {API_KEY}"},
        timeout=10.0,
    ) as client:
        # Get labs
        resp = await client.get("/items/")
        resp.raise_for_status()
        items = resp.json()
        labs = [i for i in items if i.get("type") == "lab"]
        print("=== Available Labs ===")
        for lab in labs:
            print(f"  {lab['id']}: {lab.get('title', 'N/A')}")

        # For each lab, get pass rates
        print("\n=== Scores / Pass Rates ===")
        for lab in labs:
            lab_id = lab["id"]
            try:
                resp = await client.get("/analytics/pass-rates", params={"lab": lab_id})
                resp.raise_for_status()
                rates = resp.json()
                print(f"\n--- {lab_id}: {lab.get('title', '')} ---")
                for r in rates:
                    print(f"  Task {r.get('task_id', '?')}: avg_score={r.get('avg_score', 'N/A')}, attempts={r.get('avg_attempts', 'N/A')}")
            except Exception as e:
                print(f"\n--- {lab_id}: Error - {e} ---")

            # Completion rate
            try:
                resp = await client.get("/analytics/completion-rate", params={"lab": lab_id})
                resp.raise_for_status()
                cr = resp.json()
                print(f"  Completion: {cr.get('passed', 0)}/{cr.get('total', 0)} ({cr.get('rate', 0)*100:.1f}%)")
            except Exception as e:
                print(f"  Completion rate error: {e}")

            # Top learners
            try:
                resp = await client.get("/analytics/top-learners", params={"lab": lab_id, "limit": 5})
                resp.raise_for_status()
                top = resp.json()
                print(f"  Top learners:")
                for t in top:
                    print(f"    {t.get('name', '?')}: avg={t.get('avg_score', 'N/A')}")
            except Exception as e:
                print(f"  Top learners error: {e}")

asyncio.run(main())
