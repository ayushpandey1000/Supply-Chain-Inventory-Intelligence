import pandas as pd
df=pd.read_csv("data/DataCoSupplyChainDataset.csv",encoding="latin1")
# print("Original Shape",df.shape)
# print("Missing Value",df.isnull().sum().sort_values(ascending=False).head(10))
# print("Duplicates",df.duplicated().sum())
# print("Data Cleaning strategy check completed")

columns_to_drop=[
    "Customer Email","Customer Fname","Customer Lname","Customer Street","Customer Password",
    "Customer Zipcode","Product Description","Product Image","Product Status"
]
df=df.drop(columns=columns_to_drop)
# print("Shape after",df.shape)
# print("Remaining Columns",df.columns.tolist())

# print("Missing values before handling",df.isnull().sum().sort_values(ascending=False).head(10))
date_columns=["order date (DateOrders)","shipping date (DateOrders)"]
for col in date_columns:
    df[col]=pd.to_datetime(df[col],errors="coerce")
    print(f"{col}")
    print("Invalid Dates",df[col].isna().sum())
    print("Data type",df[col].dtype)
# print("Missing values after date conversion",df.isnull().sum().sort_values(ascending=False).head(10))

df = df.drop(columns=["Order Zipcode"])
# print("Shape after handling missing values:", df.shape)
# print("\nRemaining missing values:", df.isnull().sum().sum())

print("Final dataset",df.shape)
print("Total Missing Values",df.isnull().sum())
print("Duplicated",df.duplicated().sum())
print("Date Column Types",df[["order date (DateOrders)","shipping date (DateOrders)"]].dtypes)

df.to_csv(
    "data/DataCoSupplyChain_Cleaned.csv",
    index=False
)

print("Saved Successfully")