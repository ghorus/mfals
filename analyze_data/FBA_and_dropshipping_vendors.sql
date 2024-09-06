SELECT DISTINCT p.location AS country, p.product_category AS industry
FROM vendors v
INNER JOIN products p
ON v.product_id = p.id
ORDER BY country ASC;
