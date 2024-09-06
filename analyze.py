import sqlite3
import csv
# Define a function to execute a query from a file and print the result
def execute_query(file_path, conn):
    with open(file_path, 'r') as file:
        query = file.read()
    
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    
    # Fetch column names
    columns = [description[0] for description in cursor.description]
    
    output_file = file_path.replace('.sql', '.csv')

    # Write results to a CSV file
    with open(output_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        
        # Write header
        csvwriter.writerow(columns)
        
        # Write rows
        csvwriter.writerows(results)
    
    print(f"Results saved to {output_file}")

def main():
    # List of database files
    base_db = "generate_sample_data/"
    db_files = [
        'post_sales/post_sales_refunds.db',
        'online_orders/online_orders_pickup_delivery_times.db',
        'products/products.db',
        'ratings/ratings.db',
        'online_orders/online_orders_pickup_delivery_times.db',
        'post_sales/post_sales_refunds.db',
        'products/products.db',
    ]
    # List of SQL files
    base_sql = 'analyze_data/'
    sql_files = [
        'vendors_compliance.sql',
        'retail_routing.sql',
        'products_logistics.sql',
        'customer_ratings.sql',
        'tracking_shipping.sql',
        'post_sales_refurbish.sql',
        'FBA_and_dropshipping_vendors.sql'
    ]

    # Execute each query file and print results
    for i in range(7):
        # Establish database connection
        db_path = f'{base_db}{db_files[i]}'
        sql_path = f'{base_sql}{sql_files[i]}'
        conn = sqlite3.connect(db_path)

        #combine databases for sql to execute properly
        if i == 5:
            conn.execute("ATTACH DATABASE 'generate_sample_data/products/products.db' AS products_db") 
        if i == 6:
            conn.execute("ATTACH DATABASE 'generate_sample_data/vendors/vendors.db' AS products_db") 
        execute_query(sql_path, conn)

    # Close the database connection
    conn.close()

if __name__ == "__main__":
    main()
