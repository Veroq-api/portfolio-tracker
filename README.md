# Portfolio Tracker

[![License](https://img.shields.io/badge/license-MIT-2EE89A)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9+-2EE89A)](https://python.org)
[![VEROQ](https://img.shields.io/badge/powered%20by-VEROQ-2EE89A)](https://veroq.ai)

Real-time portfolio monitoring with SSE streaming, trade signals, and sentiment tracking. Powered by [VEROQ](https://veroq.ai).

## Quick Start

```bash
pip install veroq
export VEROQ_API_KEY=vq_live_xxx
python tracker.py NVDA AAPL MSFT TSLA GOOGL
```

## Features

- Live price streaming via SSE
- Composite trade signals (0-100) per holding
- Sentiment shift alerts
- Portfolio-level risk assessment
- Earnings proximity warnings

## Links

- [VEROQ](https://veroq.ai) | [Python SDK](https://github.com/Veroq-api/veroq-python) | [Cookbook](https://github.com/Veroq-api/veroq-cookbook)