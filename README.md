# public-record-benchmarks

Reproducible latency, schema stability, and live dataset benchmarks for US federal contract cuts, SEC EDGAR lapsed LEIs, OpenFDA/NPPES healthcare feeds, and software supply-chain indexes published across **[LiveAgentData](https://liveagentdata.com)**, **[LiveGovContracts](https://livegovcontracts.com)**, **[EnterpriseSalesData](https://enterprisesalesdata.com)**, **[OffMarketSaaS](https://offmarketsaas.com)**, and **[AgentWhitelist](https://agentwhitelist.com)**.

## Featured Verified Slices (2026)

- [Defense Contract Deobligations (Agency 097 - 7,077 records)](https://livegovcontracts.com/data/fed-contract-cuts/us/097)
- [Delaware Corporate Lapsed LEI Filers (US-DE - 9,673 records)](https://enterprisesalesdata.com/data/lapsed-lei/us-de)
- [Texas EPA Formal Enforcement Liabilities (US-TX)](https://distressedpropertydata.com/data/epa-liabilities/us/tx)

```bash
python3 scripts/bench.py
python3 -m unittest discover -s test
```
