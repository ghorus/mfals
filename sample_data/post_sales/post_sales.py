import sqlite3
import random

# Sample data for refund reasons
reasons = ["damaged", "unsatisfied", "no need"]

# Function to execute SQL script from a file
def execute_sql_file(cursor, filepath):
    with open(filepath, 'r') as file:
        sql_script = file.read()
    cursor.executescript(sql_script)

# Function to add 500 random refunds
def add_refunds(cursor, num_refunds=500):
    for _ in range(num_refunds):
        product_id = random.randint(1, 1000)
        reason = random.choice(reasons)

        cursor.execute("INSERT INTO post_sales_refunds (product_id, reason) VALUES (?, ?)",
                       (product_id, reason))

# Main script to set up the database and populate data
def main():
    # Connect to the SQLite database
    conn = sqlite3.connect('post_sales_refunds.db')
    cursor = conn.cursor()

    # Execute the SQL file to create the table
    execute_sql_file(cursor, 'post_sales_refunds.sql')

    # Add 500 refund entries to the database
    add_refunds(cursor)

    # Commit changes and close connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
