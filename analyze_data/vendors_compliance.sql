SELECT COUNT(*) AS damaged_packages
FROM post_sales_refunds
WHERE reason = 'damaged';
