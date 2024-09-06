-- Lowest, highest, and average ratings for all products
-- SELECT 
--     MIN(rating) AS lowest_rating, 
--     MAX(rating) AS highest_rating, 
--     AVG(rating) AS avg_rating
-- FROM ratings;

-- Top 10 products with the highest ratings
SELECT product_id, AVG(rating) AS avg_rating
FROM ratings
GROUP BY product_id
ORDER BY avg_rating DESC
LIMIT 30;
