import pandas as pd

# Read all three CSV files
files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]

dfs = [pd.read_csv(file) for file in files]

# Combine them
df = pd.concat(dfs, ignore_index=True)

# Keep only Pink Morsels
df = df[df["product"] == "pink morsels"]

# Remove $ sign and convert price to float
df["price"] = df["price"].replace("[$]", "", regex=True).astype(float)

# Calculate sales
df["sales"] = df["quantity"] * df["price"]

# Keep required columns
output = df[["sales", "date", "region"]]

# Save output
output.to_csv("formatted_output.csv", index=False)

print("formatted_output.csv created successfully!")