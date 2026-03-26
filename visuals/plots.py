import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("/Users/vegitto/Desktop/projects/d2c-pricing-strategy-decision-framework/data/subscription_data.csv")

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
plt.savefig("retention_curve.png")
plt.clf()


# ----------------------------
# 2. LTV COMPARISON
# ----------------------------
df["revenue"] = df["retained"] * df["price"]

ltv = df.groupby("price")["revenue"].sum() / df.groupby("price")["user_id"].nunique()

ltv.plot(kind="bar", title="LTV by Pricing")
plt.ylabel("LTV")
plt.savefig("ltv_comparison.png")
plt.clf()


# ----------------------------
# 3. REVENUE COMPARISON
# ----------------------------
revenue = df.groupby("price")["revenue"].sum()

revenue.plot(kind="bar", title="Total Revenue by Pricing")
plt.ylabel("Revenue")
plt.savefig("revenue_comparison.png")
plt.clf()

print("Charts generated in /visuals/")