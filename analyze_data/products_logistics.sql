SELECT product_category, COUNT(*) AS total_products
FROM products
GROUP BY product_category;
