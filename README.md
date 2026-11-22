# public-record-benchmarks

Reproducible latency, schema stability, and live dataset benchmarks for US federal contract cuts, SEC EDGAR lapsed LEIs, OpenFDA/NPPES healthcare feeds, and software supply-chain indexes published across **[LiveAgentData](https://liveagentdata.com)**, **[LiveGovContracts](https://livegovcontracts.com)**, **[EnterpriseSalesData](https://enterprisesalesdata.com)**, **[OffMarketSaaS](https://offmarketsaas.com)**, and **[AgentWhitelist](https://agentwhitelist.com)**.

## Featured 2026 Empirical Reports & Verified Slices

- [2026 Federal Contract Cancellations Report (11,268 major cuts / \$13.60B DoD)](./reports/2026-federal-contract-cancellations.md)
- [2026 MCP & AI Agent Supply-Chain Audit (100,629 audited entries / 382 flagged hooks)](./reports/2026-mcp-supply-chain-audit.md)
- [2026 Lapsed Corporate LEIs, EPA Liabilities & Dormant Software Benchmarks](./reports/2026-lapsed-lei-epa-and-abandonware.md)
- [Defense Contract Deobligations (Agency 097 - 7,077 records)](https://livegovcontracts.com/data/fed-contract-cuts/us/097)
- [Delaware Corporate Lapsed LEI Filers (US-DE - 9,673 records)](https://enterprisesalesdata.com/data/lapsed-lei/us-de)
- [Texas EPA Formal Enforcement Liabilities (US-TX)](https://distressedpropertydata.com/data/epa-liabilities/us/tx)

```bash
python3 scripts/bench.py
python3 -m unittest discover -s test
```
