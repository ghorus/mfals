import sqlite3
import random

# Sample data for the locations, companies, and categories
locations = ["USA", "Canada", "Germany", "France", "UK", "Australia", "Japan", "China", "Mexico", "Brazil"]
companies = ["Amazon", "eBay", "Walmart"]
categories = ["Houseware", "Baby Gear", "Pets", "Electronics", "Beauty", "Exercise"]

# Function to generate a random warehouse aisle (A-F + 1-10)
def generate_warehouse_aisle():
    letter = random.choice(['A', 'B', 'C', 'D', 'E', 'F'])
    number = random.randint(1, 10)
    return f"{letter}{number}"

# Function to execute SQL script from a file
def execute_sql_file(cursor, filepath):
    with open(filepath, 'r') as file:
        sql_script = file.read()
    cursor.executescript(sql_script)

# Function to add 1000 random products
def add_products(cursor, num_products=1000):
    for _ in range(num_products):
        location = random.choice(locations)
        company_name = random.choice(companies)
        category = random.choice(categories)
        warehouse_id = random.randint(1, 7)
        warehouse_aisle = generate_warehouse_aisle()

        cursor.execute("INSERT INTO products (location, company_name, product_category, warehouse_id, warehouse_aisle) VALUES (?, ?, ?, ?, ?)",
                       (location, company_name, category, warehouse_id, warehouse_aisle))

# Main script to set up the database and populate data
def main():
    # Connect to the SQLite database
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Execute the SQL file to create the table
    execute_sql_file(cursor, 'products.sql')

    # Add 1000 products to the database
    add_products(cursor)

    # Commit changes and close connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
