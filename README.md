# Project Name
MFALS SQL Query Request Reply 

## Project Overview
A one-page website displaying data

[The Website here](https://mfals.onrender.com/)

**Note:** Please note that the website currently uses the "Free" plan on render.com because of my financial situation.

**Purpose:** MFALS Recruiter asked for a complex SQL query, so the purpose of this project is to display sample data queries. The sample datas generated are related to MFALS, such as:

### vendor compliance 
**Scenario**: A management team wants to monitor total number of packages damaged and assess whether to take action or not.
- **location on website:** vendors_compliance.csv
- [SQL query for this table](https://github.com/ghorus/mfals/blob/main/analyze_data/vendors_compliance.sql)
- **Output:** Total packages reported as 'damaged' by customers'

### retail routing
**Scenario**: Management wants to get information on which packages aren't being delivered on time for it's special "1 Week Deliveries".
- **location on website:** retail_routing.csv
- [SQL query](https://github.com/ghorus/mfals/blob/main/analyze_data/retail_routing.sql)
- **Output**: product_id, delivery_time, track_number, driver_id ordered by longest delivery time first

### products logistics
**Scenario**: Operations team wants current inventory information for each product industry category:
- **location on website:** products_logistics.csv
- [SQL query](https://github.com/ghorus/mfals/blob/main/analyze_data/products_logistics.sql)
- **Output:** A total count of products for baby gear, exercise products, pet products, beauty, houseware, and electronics

### post sales services
**Scenario**: Management needs information on which products were returned simply as "no need" so that the products can be put up for resale.
- **location on website:** products_logistics.csv
- [SQL query](https://github.com/ghorus/mfals/blob/main/analyze_data/post_sales_refurbish.sql)

### tracking and shipping
**Scenario**: Operations team wants to keep track of how many packages were delivered without a track number to assess whether to take action in order to minimize mislabeling. 
- **location on website**: tracking_shipping.csv
- [SQL query](https://github.com/ghorus/mfals/blob/main/analyze_data/tracking_shipping.sql)
- **Output:** product_id, delivery_time, driver_id to ordered by latest delivery times

### FBA & dropshipping
**Scenario**: Management wants to see which countries their products are being shipped from and what kinds of products.
- **location on website:** FBA_and_dropshipping_vendors.csv
- [SQL query](https://github.com/ghorus/mfals/blob/main/analyze_data/FBA_and_dropshipping_vendors.sql)
- **Output:** country, industry of products
