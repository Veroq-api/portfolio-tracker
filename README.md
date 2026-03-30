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

## Example Output

```
Tracking: NVDA, AAPL, MSFT, TSLA

NVDA    $   167.46   -2.21%  Signal: HOLD       (50/100)
AAPL    $   248.80   +0.33%  Signal: LEAN_BUY   (63/100)
MSFT    $   356.77   -6.57%  Signal: HOLD       (45/100)
TSLA    $   361.83   -1.67%  Signal: HOLD       (50/100)

============================================================
Portfolio Signal: 52/100
Bullish: AAPL
```

## How It Works

1. Queries VEROQ for each ticker's price, technicals, and sentiment
2. Computes composite trade signal (0-100) per holding
3. Aggregates portfolio-level risk assessment
4. Flags bullish/bearish positions

## Features

- Live price streaming via SSE
- Composite trade signals (0-100) per holding
- Sentiment shift alerts
- Portfolio-level risk assessment
- Earnings proximity warnings

## Links

- [VEROQ](https://veroq.ai) | [Python SDK](https://github.com/Veroq-api/veroq-python) | [Cookbook](https://github.com/Veroq-api/veroq-cookbook)