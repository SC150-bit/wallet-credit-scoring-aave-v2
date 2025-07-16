import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

# === STEP 1: Load JSON data ===
with open("user-wallet-transactions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# === STEP 2: Group transactions by wallet ===
wallets = defaultdict(list)
for txn in data:
    wallet = txn.get("userWallet")  # Fixed from 'user' to 'userWallet'
    if wallet:
        wallets[wallet].append(txn)

# === STEP 3: Feature Engineering ===
def extract_features(transactions):
    features = {
        "total_txns": len(transactions),
        "deposit": 0,
        "borrow": 0,
        "repay": 0,
        "redeem": 0,
        "liquidation": 0
    }
    for txn in transactions:
        action = txn.get("action", "").lower()
        if "deposit" in action:
            features["deposit"] += 1
        elif "borrow" in action:
            features["borrow"] += 1
        elif "repay" in action:
            features["repay"] += 1
        elif "redeem" in action:
            features["redeem"] += 1
        elif "liquidation" in action:
            features["liquidation"] += 1
    return features

# === STEP 4: Scoring Logic ===
def score_wallet(features):
    score = 0
    score += features["deposit"] * 5
    score += features["repay"] * 4
    score += features["borrow"] * 2
    score -= features["liquidation"] * 10
    score -= features["redeem"] * 2
    score += features["total_txns"] * 0.5
    return max(0, min(int(score), 1000))  # Clamp score between 0 and 1000

# === STEP 5: Apply scoring and prepare results ===
wallet_scores = []
for wallet, txns in wallets.items():
    feats = extract_features(txns)
    score = score_wallet(feats)
    wallet_scores.append({
        "wallet": wallet,
        "score": score,
        **feats
    })

# === STEP 6: Save scores to CSV ===
df = pd.DataFrame(wallet_scores)
df.to_csv("wallet_scores.csv", index=False)
print("✅ Saved scores to 'wallet_scores.csv'.")

# === STEP 7: Plot score distribution ===
plt.figure(figsize=(10, 6))
plt.hist(df["score"], bins=np.arange(0, 1100, 100), edgecolor="black")
plt.title("Wallet Score Distribution")
plt.xlabel("Score Range")
plt.ylabel("Number of Wallets")
plt.grid(True)
plt.savefig("score_distribution.png")
print("✅ Saved score distribution plot as 'score_distribution.png'.")