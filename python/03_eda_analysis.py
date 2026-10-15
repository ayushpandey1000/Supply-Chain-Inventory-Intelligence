# import pandas as pd
# import matplotlib.pyplot as plt
# df = pd.read_csv("data/DataCoSupplyChain_Cleaned.csv",parse_dates=["order date (DateOrders)",
# "shipping date (DateOrders)"])

# total_orders=df["Order Id"].nunique()
# total_sales=df["Sales"].sum()
# total_profit=df["Order Profit Per Order"].sum()
# avg_order_value=df.groupby("Order Id")["Sales"].sum().mean()
# late_delivery_rate=(
#     df["Late_delivery_risk"].mean()*100
# )
# # print("Total Orders",total_orders)
# # print("Total Orders Item",df["Order Item Id"].nunique())
# # print("Total Slaes",round(total_sales,2))
# # print("Total Profit",round(total_profit,2))
# # print("Avg slaes per order",round(avg_order_value,2))
# # print("Late Delivery risk rate",round(late_delivery_rate,2),"%")

# df["Order Month"]=df["order date (DateOrders)"].dt.to_period("M").astype(str)
# monthly_sales=df.groupby("Order Month")["Sales"].sum()
# # plt.figure(figsize=(12,15))
# # monthly_sales.plot(kind="line",marker="o")
# # plt.title("Monthly Sales Trend")
# # plt.xlabel("Month")
# # plt.ylabel("Sales")
# # plt.xticks(rotation=45)
# # plt.tight_layout()
# # plt.show()

# category_performance=df.groupby("Category Name").agg(Total_sales=("Sales","sum"),
# Total_Profit_Indicator=("Order Profit Per Order","sum"),Units_Sold=("Order Item Quantity","sum")).sort_values("Total_sales",ascending=False)
# # print(category_performance.round(2))
# top_categories=category_performance.head(10)
# # plt.figure(figsize=(12,6))
# # top_categories["Total_sales"].sort_values().plot(kind="barh")
# # plt.title("Top 10 Product Categories by Sales")
# # plt.xlabel("Total Sales")
# # plt.ylabel("Category")
# # plt.tight_layout()
# # plt.show()

# product_performance=df.groupby("Product Name").agg(Total_sales=("Sales","sum"),Total_Profit_Indicator=("Order Profit Per Order","sum"),Unit_Sold=("Order Item Quantity","sum")).sort_values("Total_sales",ascending=False)
# # print(product_performance.head(10).round(2))

# region_performance = df.groupby("Order Region").agg(
#     Total_Sales=("Sales", "sum"),
#     Total_Profit_Indicator=("Order Profit Per Order", "sum"),
#     Total_Orders=("Order Id", "nunique"),
#     Late_Deliveries=("Late_delivery_risk", "sum")
# )
# region_performance["Late_Delivery_Rate_%"] = (
#     region_performance["Late_Deliveries"]
#     / df.groupby("Order Region")["Order Id"].count()
#     * 100
# )
# region_performance = region_performance.sort_values(
#     "Total_Sales", ascending=False
# )
# # print(region_performance.round(2))
# # top_regions = region_performance.head(10)
# # plt.figure(figsize=(12, 6))
# # top_regions["Total_Sales"].sort_values().plot(kind="barh")
# # plt.title("Top 10 Regions by Sales")
# # plt.xlabel("Total Sales")
# # plt.ylabel("Region")
# # plt.tight_layout()
# # plt.show()

# shipping_performance=df.groupby("Shipping Mode").agg(
#     Total_sales=("Sales","sum"),
#     Total_orders=("Order Id","nunique"),
#     Total_items=("Order Item Id","count"),
#     Late_Deliveries=("Late_delivery_risk","sum")
# )
# shipping_performance["Late_Delivery_Rate_%"]=(
#     shipping_performance["Late_Deliveries"] / df.groupby("Shipping Mode")["Order Item Id"].count()*100)
# shipping_performance=shipping_performance.sort_values("Late_Delivery_Rate_%",ascending=False)
# print(shipping_performance.round(2))
# plt.figure(figsize=(10, 5))
# shipping_performance["Late_Delivery_Rate_%"].plot(
#     kind="bar", rot=0
# )
# plt.title("Late Delivery Rate by Shipping Mode")
# plt.xlabel("Shipping Mode")
# plt.ylabel("Late Delivery Rate (%)")
# plt.tight_layout()
# plt.show()

import pandas as pd

df = pd.read_csv(
    r"C:\SQLData\DataCoSupplyChain_Cleaned.csv",
    usecols=["order date (DateOrders)", "shipping date (DateOrders)"],
    nrows=5
)

print(df.to_string(index=False))