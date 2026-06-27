import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

print("=== BEFORE CLEANING ===")
before_nulls = df.isnull().sum().sum()
before_shape = df.shape
print(f"Shape: {before_shape}")
print(f"Nulls:\n{df.isnull().sum()}")
print(f"Duplicates: {df.duplicated().sum()}")

df.drop_duplicates(inplace=True)
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df.drop(columns=["Cabin"], inplace=True)
df.columns = df.columns.str.lower().str.strip()

df.to_csv("Titanic_Cleaned.csv", index=False)

print("\n=== AFTER CLEANING ===")
print(f"Shape: {df.shape}")
print(f"Nulls:\n{df.isnull().sum()}")

# Save summary report
with open("cleaning_report.txt", "w") as f:
    f.write("DATA CLEANING REPORT - TITANIC DATASET\n")
    f.write("="*40 + "\n")
    f.write(f"Original shape: {before_shape}\n")
    f.write(f"Cleaned shape: {df.shape}\n")
    f.write(f"Nulls fixed: {before_nulls}\n")
    f.write("Columns dropped: Cabin\n")
    f.write("Columns standardized: all lowercase\n")

print("Report saved as cleaning_report.txt ✅")
print("Saved as Titanic_Cleaned.csv ✅")