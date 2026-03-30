"""Real-time portfolio tracker powered by VEROQ."""
import sys
from veroq import VeroqClient

client = VeroqClient()
tickers = sys.argv[1:] if len(sys.argv) > 1 else ["NVDA", "AAPL", "MSFT", "TSLA"]

print(f"Tracking: {', '.join(tickers)}\n")

total_value = 0
signals = []

for ticker in tickers:
    result = client.ask(f"{ticker} price technicals sentiment")
    data = result.get("data", {})
    price_data = data.get("ticker", {}).get("price", {})
    price = price_data.get("current", 0)
    change = price_data.get("change_pct", 0)

    ts = result.get("trade_signal", {})
    action = ts.get("action", "?")
    score = ts.get("score", 0)

    print(f"{ticker:6s}  ${price:>10.2f}  {change:>+6.2f}%  Signal: {action.upper():10s} ({score}/100)")
    signals.append({"ticker": ticker, "score": score, "action": action})

print(f"\n{'='*60}")
avg_score = sum(s["score"] for s in signals) / len(signals) if signals else 0
print(f"Portfolio Signal: {avg_score:.0f}/100")

buys = [s for s in signals if "buy" in s["action"]]
sells = [s for s in signals if "sell" in s["action"]]
if buys:
    print(f"Bullish: {', '.join(s['ticker'] for s in buys)}")
if sells:
    print(f"Bearish: {', '.join(s['ticker'] for s in sells)}")
