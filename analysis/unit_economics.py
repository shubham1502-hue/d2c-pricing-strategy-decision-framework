import pandas as pd

# ----------------------------
# LOAD DATA
# ----------------------------
df = pd.read_csv(".../data/subscription_data.csv")

print("\n Data Loaded")
print(df.head())


# ----------------------------
# BASIC SANITY CHECKS
# ----------------------------
print("\n Dataset Shape:", df.shape)
print("\n Unique Users:", df["user_id"].nunique())


# ----------------------------
# 1. CONVERSION RATE (Month 1 only)
# ----------------------------
conversion = (
    df[df["month"] == 1]
    .groupby("price")["converted"]
    .mean()
)

print("\n Conversion Rate by Price:")
print(conversion)


# ----------------------------
# 2. RETENTION ANALYSIS
# ----------------------------
retention = (
    df.groupby(["price", "month"])["retained"]
    .mean()
    .reset_index()
)

print("\n Retention by Price & Month:")
print(retention)


# ----------------------------
# 3. ACTIVE USERS (IMPORTANT FOR INTUITION)
# ----------------------------
active_users = (
    df.groupby(["price", "month"])["retained"]
    .sum()
    .reset_index()
)

print("\n👥 Active Users by Price & Month:")
print(active_users)


# ----------------------------
# 4. REVENUE CALCULATION
# ----------------------------
df["revenue"] = df["retained"] * df["price"]

revenue = df.groupby("price")["revenue"].sum()

print("\n Total Revenue by Price:")
print(revenue)


# ----------------------------
# 5. LTV CALCULATION
# ----------------------------
users = df.groupby("price")["user_id"].nunique()

ltv = revenue / users

print("\n LTV by Price:")
print(ltv)


# ----------------------------
# 6. AVERAGE LIFETIME (IN MONTHS)
# ----------------------------
lifetime = (
    df.groupby(["price", "user_id"])["retained"]
    .sum()
    .groupby("price")
    .mean()
)

print("\n⏳ Average Lifetime (Months):")
print(lifetime)


# ----------------------------
# 7. ARPU (AVG REVENUE PER USER PER MONTH)
# ----------------------------
monthly_revenue = (
    df.groupby(["price", "month"])["revenue"]
    .sum()
    .groupby("price")
    .mean()
)

monthly_active_users = (
    df.groupby(["price", "month"])["retained"]
    .sum()
    .groupby("price")
    .mean()
)

arpu = monthly_revenue / monthly_active_users

print("\n ARPU (Monthly):")
print(arpu)


# ----------------------------
# 8. CAC PAYBACK (ASSUMPTION-BASED)
# ----------------------------
CAC = 300  # Assumed

payback_period = CAC / arpu

print("\n CAC Payback Period (Months):")
print(payback_period)


# ----------------------------
# FINAL SUMMARY (THIS IS GOLD)
# ----------------------------
summary = pd.DataFrame({
    "Conversion Rate": conversion,
    "Total Revenue": revenue,
    "LTV": ltv,
    "Avg Lifetime (Months)": lifetime,
    "ARPU": arpu,
    "CAC Payback (Months)": payback_period
})

print("\n🔥 FINAL SUMMARY:")
print(summary)