#!/usr/bin/env python3
"""Reproducible latency & status check across live Shinn public-record & AI-search endpoints."""
import json
import time
import urllib.request

ENDPOINTS = [
    "https://liveagentdata.com/feeds.json",
    "https://livegovcontracts.com/feeds.json",
    "https://healthcaredatafeeds.com/feeds.json",
    "https://agentwhitelist.com/.well-known/mcp.json",
    "https://offmarketsaas.com/.well-known/mcp.json",
    "https://tinkermcp.com/.well-known/mcp.json",
]

def check_endpoint(url, timeout=10):
    t0 = time.perf_counter()
    req = urllib.request.Request(url, headers={"User-Agent": "public-record-benchmarks/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        body = r.read()
        ms = round((time.perf_counter() - t0) * 1000, 1)
        return {"url": url, "status": r.status, "bytes": len(body), "latency_ms": ms}

if __name__ == "__main__":
    results = []
    for u in ENDPOINTS:
        try:
            results.append(check_endpoint(u))
        except Exception as exc:
            results.append({"url": u, "error": str(exc)})
    print(json.dumps({"checked": len(results), "results": results}, indent=2))
