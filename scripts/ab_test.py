import pandas as pd
import numpy as np
from scipy import stats

# Load data
df = pd.read_csv("data/ab_test_data.csv")
# Clean column names
df.columns = df.columns.str.strip()

# Conversion rates
conversion = df.groupby("group")["converted"].mean()

print("=== Conversion Rates ===")
print(conversion)

# Separate groups
group_A = df[df["group"] == "A"]["converted"]
group_B = df[df["group"] == "B"]["converted"]

# Statistical test (t-test)
t_stat, p_value = stats.ttest_ind(group_A, group_B)

print("\n=== Statistical Test ===")
print("T-statistic:", t_stat)
print("P-value:", p_value)

# Conversion lift
conversion_A = conversion["A"]
conversion_B = conversion["B"]

uplift = (conversion_B - conversion_A) / conversion_A * 100

print("\n=== Business Impact ===")
print("Conversion Lift (%):", round(uplift, 2))

# Decision
alpha = 0.05

print("\n=== Final Decision ===")

if p_value < alpha:
    print("Statistically significant result")
    print("👉 Deploy Version B")
else:
    print("No statistically significant difference")
    print("👉 Collect more data before decision")

# Save results
conversion.to_csv("results/conversion_summary.csv")