
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
df = pd.read_excel("customer_churn (1).xlsx")

print("First 5 records:")
print(df.head())

# 2. Basic information
print("\nShape of dataset:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nDataset information:")
df.info()

# 3. Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# 4. Remove duplicate records
print("\nDuplicate records:")
print(df.duplicated().sum())

df = df.drop_duplicates()

# 5. Handle missing values
numeric_columns = df.select_dtypes(
    include=np.number
).columns

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].mean())

categorical_columns = df.select_dtypes(
    include="object"
).columns

for column in categorical_columns:
    if df[column].isnull().any() and not df[column].mode().empty:
        df[column] = df[column].fillna(
            df[column].mode()[0]
        )

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# 6. Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# 7. Average monthly charges
print("\nAverage Monthly Charges:")
print(np.mean(df["MonthlyCharges"]))

# 8. Average customer tenure
print("\nAverage Customer Tenure:")
print(np.mean(df["Tenure"]))

# 9. Customer churn count
print("\nCustomer Churn Count:")
print(df["Churn"].value_counts())

# 10. Churn percentage
churn_percentage = (
    df["Churn"].value_counts(normalize=True) * 100
)

print("\nChurn Percentage:")
print(churn_percentage)

# 11. Visualization - Churn Count
df["Churn"].value_counts().plot(kind="bar")

plt.title("Customer Churn Count")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 12. Visualization - Monthly Charges
plt.hist(df["MonthlyCharges"], bins=10)

plt.title("Distribution of Monthly Charges")
plt.xlabel("Monthly Charges")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()

# 13. Visualization - Customer Tenure
plt.hist(df["Tenure"], bins=10)

plt.title("Distribution of Customer Tenure")
plt.xlabel("Tenure")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()

# 14. Churn based on Contract
contract_churn = pd.crosstab(
    df["Contract"], df["Churn"]
)

print("\nChurn Based on Contract:")
print(contract_churn)

contract_churn.plot(kind="bar")

plt.title("Customer Churn by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 15. Average Monthly Charges by Churn
average_charges = df.groupby(
    "Churn"
)["MonthlyCharges"].mean()

print("\nAverage Monthly Charges by Churn:")
print(average_charges)

average_charges.plot(kind="bar")

plt.title("Average Monthly Charges vs Churn")
plt.xlabel("Churn")
plt.ylabel("Average Monthly Charges")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 16. Correlation between numerical variables
correlation = df.select_dtypes(
    include=np.number
).corr()

print("\nCorrelation Matrix:")
print(correlation)

plt.figure(figsize=(8, 6))
plt.imshow(correlation, cmap="coolwarm")
plt.colorbar()

plt.xticks(
    range(len(correlation.columns)),
    correlation.columns,
    rotation=45
)

plt.yticks(
    range(len(correlation.columns)),
    correlation.columns
)

plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()
