import pandas as pd

df_asia = pd.read_csv('../data/sales_asia.csv')
df_usa = pd.read_csv('../data/sales_usa.csv')
df_europe = pd.read_csv('../data/sales_europe.csv')

df = pd.concat([df_asia, df_usa, df_europe], ignore_index=True)
df.dropna(inplace=True)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Total_Amount'] = df['Quantity'] * df['Unit_Price'] * (1 - df['Discount'])

df.to_csv('../data/cleaned_sales.csv', index=False)
print("Cleaned data saved successfully.")
