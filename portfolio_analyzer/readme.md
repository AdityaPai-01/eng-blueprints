# Portfolio Intelligence Engine

A mid-sized, modular data analytics pipeline built using **NumPy** and **Pandas** to analyze financial health, evaluate portfolio risk, and simulate future asset performance.

This project is a dedicated learning exercise designed to explore the fundamentals of data science, functional software engineering design, and algorithmic finance.

---

## Key Features

- **Transaction Ingestion & Cleaning:** Standardizes and sanitizes messy multi-year transaction logs using Pandas string parsing and regular expressions.
- **Market Data Alignment:** Programmatically fetches historical asset and benchmark data (`yfinance`) and aligns timestamps using advanced merging techniques like `pandas.merge_asof`.
- **Risk & Performance Metrics:** Harnesses NumPy vectorized operations to calculate rolling volatility, asset correlation matrices, Sharpe Ratios, and portfolio Beta.
- **Predictive Monte Carlo Simulations:** Executes 10,000 randomized asset price projections to model future portfolio distributions and milestone probabilities.

---

## Pipeline Workflow

1. **Ingestion (`src/data_ingestion.py`):** Parses raw financial statements, normalizes action types (Buy, Sell, Deposit), and flags anomalies.
2. **Market Integration (`src/market_data.py`):** Downloads historical daily adjusted closes and fills weekend/holiday gaps to map transactions to market value.
3. **Analytics Engine (`src/metrics.py`):** Evaluates risk parameters, calculates asset weights, and runs matrix multiplications for optimized returns.
4. **Execution (`main.py`):** Orchestrates the full pipeline and prints out the final portfolio intelligence report.

---

## Development & AI Disclosure

This repository serves as a pedagogical sandbox for data science exploration. In line with modern software development practices, **Generative AI** was utilized responsibly throughout its creation to accelerate code scaffolding, brainstorm architectural patterns, and design robust testing edge cases. All algorithmic implementations, data assumptions, and logical structures have been meticulously verified, reviewed, and documented manually to ensure educational integrity.
