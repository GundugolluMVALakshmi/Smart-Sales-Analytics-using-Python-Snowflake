import pandas as pd
import snowflake.connector
from snowflake.connector.errors import ProgrammingError


df = pd.read_csv('../data/cleaned_sales.csv')

# Snowflake connection (dummy credentials – replace with yours)
conn = snowflake.connector.connect(
    user='YOUR_USERNAME',
    password='YOUR_PASSWORD',
    account='YOUR_ACCOUNT',
    warehouse='YOUR_WAREHOUSE',
    database='YOUR_DATABASE',
    schema='PUBLIC'
)

cursor = conn.cursor()

try:
  
    cursor.execute("""
    CREATE OR REPLACE TABLE SALES_DATA (
        Order_ID STRING,
        Date DATE,
        Region STRING,
        Product STRING,
        Quantity INT,
        Unit_Price FLOAT,
        Discount FLOAT,
        Total_Amount FLOAT
    );
    """)

   
    for index, row in df.iterrows():
        cursor.execute("""
            INSERT INTO SALES_DATA 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, tuple(row))

    
    conn.commit()
    print("Data inserted into Snowflake successfully.")

except ProgrammingError as e:
    print(f"Error occurred: {e}")
    conn.rollback()

finally:
    cursor.close()
    conn.close()
