import sqlite3
import random

# Sample data for first names and last names
first_names = [
    "John", "Jane", "Michael", "Sarah", "William", "Emma", "David", "Olivia", 
    "James", "Sophia", "Robert", "Isabella", "Mary", "Liam", "Charles", "Emily", 
    "Daniel", "Abigail", "Lucas", "Charlotte", "Joseph", "Benjamin", "Matthew", 
    "Elijah", "Henry", "Mason", "Ethan", "Ava", "Alexander", "Mia"
]

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", 
    "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", 
    "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson", 
    "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Walker"
]

# Employment statuses
statuses = ["employed", "fired", "quit"]

# Departments
departments = ["Human Resources", "Sales", "Marketing", "Operations", "Finance", "Administration", "Production"]

# Function to execute SQL script from a file
def execute_sql_file(cursor, filepath):
    with open(filepath, 'r') as file:
        sql_script = file.read()
    cursor.executescript(sql_script)

# Function to add 1000 random employees
def add_employees(cursor, num_employees=1000):
    for _ in range(num_employees):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        status = random.choice(statuses)
        department = random.choice(departments)
        cursor.execute("INSERT INTO employees (first_name, last_name, status, department) VALUES (?, ?, ?, ?)",
                       (first_name, last_name, status, department))

# Main script to set up the database and populate data
def main():
    # Connect to the SQLite database
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()

    # Execute the SQL file to create the table
    execute_sql_file(cursor, 'employees.sql')

    # Add 1000 employees to the database
    add_employees(cursor)

    # Commit changes and close connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
