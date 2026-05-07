import pandas as pd
import numpy as np
from pathlib import Path

# ----------------------------
# CONFIG
# ----------------------------
NUM_USERS = 500
MONTHS = list(range(1, 13))
np.random.seed(42)

PRICE_OPTIONS = [999, 699]

CONVERSION_RATES = {
    999: 0.06,
    699: 0.10
}

CHURN_RATES = {
    999: 0.25,
    699: 0.20
}

CHANNELS = ["ads", "organic", "referral"]

# ----------------------------
# DATA GENERATION
# ----------------------------
data = []

for user_id in range(1, NUM_USERS + 1):

    price = np.random.choice(PRICE_OPTIONS)
    channel = np.random.choice(CHANNELS)

    active = False  # user subscription state

    for month in MONTHS:

        converted = 0
        churned = 0
        retained = 0

        # ----------------------------
        # MONTH 1: CONVERSION
        # ----------------------------
        if month == 1:
            if np.random.rand() < CONVERSION_RATES[price]:
                active = True
                converted = 1
            else:
                active = False

        # ----------------------------
        # RETENTION LOGIC
        # ----------------------------
        if active:
            retained = 1

            # Apply churn AFTER minimum survival period
            if month > 2:
                if np.random.rand() < CHURN_RATES[price]:
                    churned = 1
                    active = False

        else:
            retained = 0
            churned = 0

        # ----------------------------
        # STORE ROW
        # ----------------------------
        data.append([
            user_id,
            month,
            price,
            converted,
            churned,
            retained,
            channel
        ])

# ----------------------------
# CREATE DATAFRAME
# ----------------------------
df = pd.DataFrame(data, columns=[
    "user_id",
    "month",
    "price",
    "converted",
    "churned",
    "retained",
    "acquisition_channel"
])

# ----------------------------
# SAVE FILE
# ----------------------------
output_path = Path(__file__).resolve().parent / "subscription_data.csv"
df.to_csv(output_path, index=False)

print(f"Dataset generated: {output_path}")
