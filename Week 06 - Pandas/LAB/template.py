"""Vectorized record report using pandas."""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("records_sample.csv")
df["percent"] = df["value"] / df["limit"] * 100
df["status"] = df["percent"].apply(lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK")
print(df)
print("\nNeeds attention:")
print(df[df["status"] != "OK"])
print("\nCounts:")
print(df.groupby("status").size())
df.to_csv("records_report.csv", index=False)
df["status"].value_counts().plot(kind="bar", title="Record status counts")
plt.tight_layout()
plt.savefig("status_counts.png")
