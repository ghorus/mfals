import sqlite3
import random

# Function to execute SQL script from a file
def execute_sql_file(cursor, filepath):
    with open(filepath, 'r') as file:
        sql_script = file.read()
    cursor.executescript(sql_script)

# Function to add random ratings
def add_ratings(cursor, num_ratings=100000):
    for _ in range(num_ratings):
        product_id = random.randint(1, 1000)
        rating = random.randint(1, 5)

        cursor.execute("INSERT INTO ratings (product_id, rating) VALUES (?, ?)",
                       (product_id, rating))

# Main script to set up the database and populate data
def main():
    # Connect to the SQLite database
    conn = sqlite3.connect('ratings.db')
    cursor = conn.cursor()

    # Execute the SQL file to create the table
    execute_sql_file(cursor, 'ratings.sql')

    # Add 500 ratings to the database
    add_ratings(cursor)

    # Commit changes and close connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
