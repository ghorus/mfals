SELECT *
FROM online_orders_pickup_delivery_times
WHERE track_number IS NULL
ORDER BY delivery_time DESC;
