import sqlite3
import random

# Function to generate random track number, with some being NULL
def generate_track_number():
    return None if random.random() < 0.2 else f"TRACK{random.randint(1000, 9999)}"

# Function to execute SQL script from a file
def execute_sql_file(cursor, filepath):
    with open(filepath, 'r') as file:
        sql_script = file.read()
    cursor.executescript(sql_script)

# Function to add 1000 random online orders with delivery times
def add_online_orders(cursor, num_orders=1000):
    for _ in range(num_orders):
        product_id = random.randint(1, 1000)
        delivery_time = random.randint(1, 10)
        track_number = generate_track_number()  # Randomly set to NULL or a track number
        driver_id = random.randint(1, 1000)

        cursor.execute("INSERT INTO online_orders_pickup_delivery_times (product_id, delivery_time, track_number, driver_id) VALUES (?, ?, ?, ?)",
                       (product_id, delivery_time, track_number, driver_id))

# Main script to set up the database and populate data
def main():
    # Connect to the SQLite database
    conn = sqlite3.connect('online_orders_pickup_delivery_times.db')
    cursor = conn.cursor()

    # Execute the SQL file to create the table
    execute_sql_file(cursor, 'online_orders_pickup_delivery_times.sql')

    # Add 1000 random online orders
    add_online_orders(cursor)

    # Commit changes and close connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
