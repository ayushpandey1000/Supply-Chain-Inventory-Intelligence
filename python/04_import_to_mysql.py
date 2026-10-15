import pandas as pd
import mysql.connector

df = pd.read_csv(
    "data/DataCoSupplyChain_Cleaned.csv",
    encoding="latin1"
)


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="supply_chain_db"
)

cursor = conn.cursor()


columns = [f"`{col}`" for col in df.columns]
column_names = ", ".join(columns)
placeholders = ", ".join(["%s"] * len(df.columns))

create_table_sql = """
CREATE TABLE IF NOT EXISTS supply_chain (
    `Type` VARCHAR(100),
    `Days for shipping (real)` INT,
    `Days for shipment (scheduled)` INT,
    `Benefit per order` DOUBLE,
    `Sales per customer` DOUBLE,
    `Delivery Status` VARCHAR(100),
    `Late_delivery_risk` INT,
    `Category Id` INT,
    `Category Name` VARCHAR(200),
    `Customer City` VARCHAR(200),
    `Customer Country` VARCHAR(100),
    `Customer Id` INT,
    `Customer Segment` VARCHAR(100),
    `Customer State` VARCHAR(100),
    `Department Id` INT,
    `Department Name` VARCHAR(200),
    `Latitude` DOUBLE,
    `Longitude` DOUBLE,
    `Market` VARCHAR(100),
    `Order City` VARCHAR(200),
    `Order Country` VARCHAR(100),
    `order date (DateOrders)` DATETIME,
    `Order Id` BIGINT,
    `Order Item Cardprod Id` BIGINT,
    `Order Item Discount` DOUBLE,
    `Order Item Discount Rate` DOUBLE,
    `Order Item Id` BIGINT,
    `Order Item Product Price` DOUBLE,
    `Order Item Profit Ratio` DOUBLE,
    `Order Item Quantity` INT,
    `Sales` DOUBLE,
    `Order Item Total` DOUBLE,
    `Order Profit Per Order` DOUBLE,
    `Order Region` VARCHAR(100),
    `Order State` VARCHAR(200),
    `Order Status` VARCHAR(100),
    `Product Card Id` BIGINT,
    `Product Name` VARCHAR(300),
    `Product Price` DOUBLE,
    `shipping date (DateOrders)` DATETIME,
    `Shipping Mode` VARCHAR(100),
    `Order Item Total Amount` DOUBLE,
    `Order Zipcode` VARCHAR(50)
)
"""

cursor.execute(create_table_sql)
conn.commit()


sql = f"""
INSERT INTO supply_chain ({column_names})
VALUES ({placeholders})
"""

df = df.astype(object).where(pd.notnull(df), None)
batch_size = 5000

try:
    for start in range(0, len(df), batch_size):
        batch = df.iloc[start:start + batch_size]

        data = [
            tuple(row)
            for row in batch.itertuples(index=False, name=None)
        ]

        cursor.executemany(sql, data)
        conn.commit()

        print(
            f"Imported {min(start + batch_size, len(df))}"
            f" / {len(df)} rows"
        )

    print("Import completed successfully!")

except Exception as e:
    conn.rollback()
    print("Import error:", e)

finally:
    cursor.close()
    conn.close()
