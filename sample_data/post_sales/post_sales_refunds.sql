-- post_sales_refunds.sql
CREATE TABLE IF NOT EXISTS post_sales_refunds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    reason TEXT NOT NULL
);
