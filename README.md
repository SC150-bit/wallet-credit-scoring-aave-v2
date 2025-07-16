# Wallet Credit Scoring using Aave V2 Transaction Data

## Overview
This project involves building a machine learning/data-driven scoring system that assigns a **credit score (0–1000)** to user wallets based solely on their historical transaction behavior with the **Aave V2 DeFi protocol**.

## Dataset
The input dataset is a large JSON file containing 100K+ wallet transactions, each consisting of:
- Wallet address (`userWallet`)
- Action (`deposit`, `borrow`, `repay`, `redeem`, `liquidationcall`)
- Timestamp, block number, asset details, etc.

## Feature Engineering
Each wallet’s transactions are grouped and the following features are extracted:
- Number of actions per type: `deposit`, `borrow`, `repay`, `redeem`, `liquidation`
- Total number of transactions

## Scoring Logic
Each wallet is scored using a custom logic:
- `+5` for each `deposit`
- `+4` for each `repay`
- `+2` for each `borrow`
- `-2` for each `redeem`
- `-10` for each `liquidation`
- `+0.5` per total transaction

Scores are clamped to the range **[0, 1000]**.

## Output Files
- `wallet_scores.csv`: Contains one row per wallet with features and the assigned score.
- `score_distribution.png`: Histogram showing distribution of wallet scores in bins of 100.

## How to Run
```bash
pip install pandas matplotlib
python main.py# wallet-credit-scoring-aave-v2
This project assigns credit scores (0–1000) to wallets based on transaction data from the Aave V2 protocol. It uses behavior analysis of actions like deposit, borrow, repay, redeem, and liquidation to rank wallets by reliability. Outputs include a score CSV, distribution chart, and detailed behavioral analysis.
