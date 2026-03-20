import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/ab_test_data.csv")
# Conversion rate
conversion = df.groupby("group")["converted"].mean()

# Plot
conversion.plot(kind='bar')

plt.title("Conversion Rate by Group")
plt.ylabel("Conversion Rate")
plt.xlabel("Group")

plt.show()