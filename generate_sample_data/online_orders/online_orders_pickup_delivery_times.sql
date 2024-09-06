CREATE TABLE IF NOT EXISTS online_orders_pickup_delivery_times (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    delivery_time INTEGER NOT NULL,
    track_number TEXT,
    driver_id INTEGER NOT NULL
);
