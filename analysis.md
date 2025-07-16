# Wallet Score Analysis Report

This report provides an analysis of user wallet scores derived from DeFi transaction data on the Aave V2 protocol. Wallets are scored from **0 to 1000** based on behavioral indicators such as deposits, repayments, borrowings, liquidations, and redemptions.

---

## 📊 Score Distribution

| Score Range | Number of Wallets |
|-------------|--------------------|
| 0–100       | 2850               |
| 100–200     | 238                |
| 200–300     | 84                 |
| 300–400     | 67                 |
| 400–500     | 58                 |
| 500–600     | 32                 |
| 600–700     | 24                 |
| 700–800     | 23                 |
| 800–900     | 15                 |
| 900–1000    | 9                  |

The distribution clearly shows that a majority of wallets fall in the **0–100** score range, indicating either inactive or risky behavior patterns.

---

## ⚠️ Behavior of Low-Scoring Wallets (Score < 200)

Low-scoring wallets (most frequent) exhibit the following behavior:
- High **redeem** and **liquidation** activity
- Low count of **deposit** and **repay** actions
- Potentially bot-like, spammy, or high-risk usage patterns

These accounts are likely not maintaining healthy positions or frequently default on borrowed assets.

---

## ✅ Behavior of High-Scoring Wallets (Score ≥ 800)

High-scoring wallets show:
- High volume of **deposits** and **repayments**
- Little to no **liquidations**
- Consistent and responsible interaction with the protocol

These wallets are reliable and exhibit patterns aligned with genuine, long-term DeFi users.

---

## 🧠 Key Insights

- A wallet’s **deposit-repay ratio** is a key determinant in scoring.
- High **liquidation** and **redeem** events heavily penalize the score.
- The model captures risk behavior well, with a meaningful separation between healthy and unhealthy DeFi participants.
- This scoring model can assist in developing credit risk metrics and fraud detection filters in DeFi platforms.

---

**📌 Note**: The score distribution chart (`score_distribution.png`) complements this report visually and is included in the project repo.