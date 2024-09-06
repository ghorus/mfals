SELECT p.id, p.warehouse_aisle, r.reason
FROM post_sales_refunds r
INNER JOIN products p
ON r.product_id = p.id
WHERE r.reason = 'no need'
ORDER BY p.warehouse_aisle;
