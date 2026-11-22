# 2026 Federal Contract Cancellations & Deobligations Report

Published by **James Shinn (Shinn Company LLC)** using live cloud records queried from [`livegovcontracts.com`](https://livegovcontracts.com).

## Scope

- **Cloud Table Size:** `11,268` major federal contract deobligation actions (`>$100,000`) audited directly in Cloudflare D1 (`flagship_fed_contract_cuts`).
- **Methodology:** Aggregates negative obligation modifications across USAspending / FPDS award modifications grouped by contracting agency code.

## Top 10 Agencies by Total Deobligated Volume

| Agency Code | Federal Agency | Cut Actions | Total Deobligated (USD Millions) | Live Slice URL |
|---|---|---:|---:|---|
| `097` | Department of Defense | 7,077 | \$13,598.74M | [Agency 097 Slice](https://livegovcontracts.com/data/fed-contract-cuts/us/097) |
| `075` | Department of Health and Human Services | 512 | \$3,240.18M | [Agency 075 Slice](https://livegovcontracts.com/data/fed-contract-cuts/us/075) |
| `089` | Department of Energy | 120 | \$1,924.86M | — |
| `036` | Department of Veterans Affairs | 1,000 | \$1,232.47M | [Agency 036 Slice](https://livegovcontracts.com/data/fed-contract-cuts/us/036) |
| `070` | Department of Homeland Security | 411 | \$994.89M | [Agency 070 Slice](https://livegovcontracts.com/data/fed-contract-cuts/us/070) |
| `047` | General Services Administration | 393 | \$829.11M | [Agency 047 Slice](https://livegovcontracts.com/data/fed-contract-cuts/us/047) |
| `019` | Department of State | 162 | \$286.46M | [Agency 019 Slice](https://livegovcontracts.com/data/fed-contract-cuts/us/019) |
| `015` | Department of Justice | 396 | \$208.49M | [Agency 015 Slice](https://livegovcontracts.com/data/fed-contract-cuts/us/015) |
| `020` | Department of the Treasury | 119 | \$208.35M | — |
| `080` | National Aeronautics and Space Administration | 160 | \$200.65M | — |

## Programmatic & AI Agent Access

- Markdown twin format: append `.md` to any slice URL above (`https://livegovcontracts.com/data/fed-contract-cuts/us/097.md`)
- Streamable HTTP MCP: `https://liveagentdata.com/mcp` ([shinnjr/liveagentdata-mcp](https://github.com/shinnjr/liveagentdata-mcp))
- Benchmark Repository: [`shinnjr/public-record-benchmarks`](https://github.com/shinnjr/public-record-benchmarks)
