import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load data
ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "data" / "subscription_data.csv")

# ----------------------------
# 1. RETENTION CURVE
# ----------------------------
retention = (
    df.groupby(["price", "month"])["retained"]
    .mean()
    .reset_index()
)

for price in retention["price"].unique():
    subset = retention[retention["price"] == price]
    plt.plot(subset["month"], subset["retained"], label=f"Price {price}")

plt.title("Retention Curve by Pricing")
plt.xlabel("Month")
plt.ylabel("Retention Rate")
plt.legend()
plt.savefig(ROOT / "retention_curve.png")
plt.clf()


# ----------------------------
# 2. LTV COMPARISON
# ----------------------------
df["revenue"] = df["retained"] * df["price"]

ltv = df.groupby("price")["revenue"].sum() / df.groupby("price")["user_id"].nunique()

ltv.plot(kind="bar", title="LTV by Pricing")
plt.ylabel("LTV")
plt.savefig(ROOT / "ltv_comparison.png")
plt.clf()


# ----------------------------
# 3. REVENUE COMPARISON
# ----------------------------
revenue = df.groupby("price")["revenue"].sum()

revenue.plot(kind="bar", title="Total Revenue by Pricing")
plt.ylabel("Revenue")
plt.savefig(ROOT / "revenue_comparison.png")
plt.clf()

print("Charts generated: retention_curve.png, ltv_comparison.png, revenue_comparison.png")
