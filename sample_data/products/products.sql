-- products.sql
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    location TEXT NOT NULL,
    company_name TEXT NOT NULL,
    product_category TEXT NOT NULL,
    warehouse_id INTEGER NOT NULL,
    warehouse_aisle TEXT NOT NULL
);
