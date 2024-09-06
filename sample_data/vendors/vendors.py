import sqlite3
import random

# Sample data for suppliers and companies
suppliers = ["Global Supply Co.", "NextGen Suppliers", "Prime Distributors", "EcoWorld Products", 
             "TechSource Inc.", "Universal Traders", "GreenField Supplies", "Allied Goods", 
             "Blue Horizon Exports", "FutureMart Solutions"]


# Function to execute SQL script from a file
def execute_sql_file(cursor, filepath):
    with open(filepath, 'r') as file:
        sql_script = file.read()
    cursor.executescript(sql_script)

# Function to add 1000 random vendors and their products
def add_vendors(cursor, num_vendors=1000):
    for i in range(1,num_vendors+1):
        supplier_name = random.choice(suppliers)
        product_id = i

        cursor.execute("INSERT INTO vendors (supplier_name, product_id) VALUES (?, ?)",
                       (supplier_name, product_id))

# Main script to set up the database and populate data
def main():
    # Connect to the SQLite database
    conn = sqlite3.connect('vendors.db')
    cursor = conn.cursor()

    # Execute the SQL file to create the table
    execute_sql_file(cursor, 'vendors.sql')

    # Add 500 vendors to the database
    add_vendors(cursor)

    # Commit changes and close connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
