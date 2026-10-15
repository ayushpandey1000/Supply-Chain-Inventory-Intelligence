import pandas as pd
df=pd.read_csv("data/DataCoSupplyChainDataset.csv",encoding="latin1")
print("Unique order id",df["Order Id"].nunique())
print("Unique order item id",df["Order Item Id"].nunique())
print("\n Negative Sales:",(df["Sales"]<0).sum())
print("\n Zero Sales:",(df["Sales"]==0).sum())
print("Negative Quantity",(df["Order Item Quantity"]<0).sum())
print("Zero Quantity",(df["Order Item Quantity"]==0).sum())
print("Negative Product Price",(df["Product Price"]<0).sum())
print("Negative Order Profit",(df["Order Profit Per Order"]<0).sum())
print("\nDelivery Status vs Late Risk:")
print(pd.crosstab(
    df["Delivery Status"],
    df["Late_delivery_risk"]
))
for col in[
    "order date (DateOrders)","shipping date (DateOrders)"
]: 
    dates=pd.to_datetime(df[col],errors="coerce")
    print(f"{col}")
    print("Invaild Dates",dates.isna().sum())
    print("Earliest",dates.min())
    print("Latest",dates.max())

constant_cols  =[col for col in df.columns if df[col].nunique(dropna=False) <=1]
print("Constant cols",constant_cols)  