# Smart-Sales-Analytics-using-Python-Snowflake

**Project Description:**
This project focuses on analyzing regional sales data from Asia, USA, and Europe. The data is processed using an ETL pipeline in Python and is then loaded into Snowflake for scalable querying and reporting. The main goal is to gain insights into sales trends, including total revenue calculations, discounts, and high-selling products by region.

**Key Technologies:**
- **Python** (Pandas for data manipulation)
- **Snowflake** (Cloud Data Warehouse for scalable storage and analytics)
- **CSV** (Sample sales data format)

**Responsibilities:**
- Designed an ETL pipeline to clean and transform raw sales data.
- Combined multi-regional sales data and generated meaningful insights.
- Loaded cleaned and transformed data into Snowflake for reporting purposes.

**Features:**
- Clean and transform data from raw CSVs.
- Push cleaned data into Snowflake for further analytics.
- Calculate total revenue with discounts applied.
- Generate insights like total sales by region, highest-selling products, etc.

**How to Run:**
1. **Install dependencies from `requirements.txt`:**
   ```bash
   pip install -r requirements.txt
````

2. **Run the ETL script to clean the data:**

   ```bash
   python scripts/etl_sales.py
   ```

3. **Load cleaned data into Snowflake:**

   ```bash
   python scripts/load_to_snowflake.py
   ```

**Sample Insights:**

* Total Sales by Region
* Highest Selling Products
* Revenue with Discounts Applied

````
