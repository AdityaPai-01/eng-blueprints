# generate_data.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(67)

# Configuration for scale
num_transactions = 220
start_date = datetime(2024, 1, 1)
tickers = ["AAPL", "MSFT", "NVDA", "TSLA", "SPY", "BTC-USD"]
memos_pool = {
    "BUY": ["Bought {qty} shares of {ticker}", "Purchased {qty} units of {ticker}", "Trade order executed: BUY {qty} {ticker}"],
    "SELL": ["Sold {qty} shares of {ticker}", "Market order fill: SELL {qty} {ticker}", "Liquidated {qty} units of {ticker}"],
    "DEPOSIT": ["Deposit from checking acct", "ACH TRANSFER FROM BANK", "Weekly payroll deposit"]
}

timestamps = []
memos = []
amounts = []
fees = []

current_date = start_date

for i in range(num_transactions):
    # Progress time randomly by 2 to 7 days per transaction to simulate real life
    current_date += timedelta(days=int(np.random.randint(2, 8)))
    if current_date > datetime(2026, 6, 1):
        break
        
    # Standardize timestamp with random times
    ts_str = current_date.strftime(f"%Y-%m-%d {np.random.randint(9,17)}:%M:%S")
    timestamps.append(ts_str)
    
    # 15% chance of a cash deposit, otherwise a buy or sell trade
    tx_type = np.random.choice(["DEPOSIT", "BUY", "SELL"], p=[0.15, 0.65, 0.20])
    
    if tx_type == "DEPOSIT":
        memos.append(np.random.choice(memos_pool["DEPOSIT"]))
        amounts.append(float(np.random.choice([500, 1000, 1500, 2500])))
        fees.append(0.0 if np.random.rand() > 0.2 else None) # Introduce missing values
    else:
        ticker = np.random.choice(tickers)
        # Randomize quantities (Crypto can have smaller fractional shares)
        qty = round(np.random.uniform(0.1, 15.0), 4) if ticker == "BTC-USD" else int(np.random.randint(1, 20))
        
        # Random price generation just for raw ledger realism
        mock_price = np.random.uniform(10, 500) if ticker != "BTC-USD" else np.random.uniform(30000, 70000)
        total_cost = round(qty * mock_price, 2)
        
        # Chaos injection: randomly mix upper and lowercase tickers in text
        chosen_ticker = ticker.lower() if np.random.rand() > 0.5 else ticker
        raw_memo = np.random.choice(memos_pool[tx_type]).format(qty=qty, ticker=chosen_ticker)
        memos.append(raw_memo)
        
        if tx_type == "BUY":
            amounts.append(-total_cost)
        else:
            amounts.append(total_cost)
            
        # Fees: brokerages charge small flat or percentage fees, inject some NaNs too
        fees.append(np.random.choice([0.99, 1.99, 4.95, 0.0, None], p=[0.3, 0.3, 0.1, 0.1, 0.2]))

df = pd.DataFrame({
    "Timestamp": timestamps,
    "Memo": memos,
    "Amount": amounts,
    "Tx_Fee": fees
})

# Shuffle slightly to simulate out-of-order clearing logs
df = df.sample(frac=1).reset_index(drop=True)

df.to_csv("data_dir/raw_transactions.csv", index=False)
print(f"Successfully generated a chaotic dataset with {len(df)} entries in data/raw_transactions.csv!")