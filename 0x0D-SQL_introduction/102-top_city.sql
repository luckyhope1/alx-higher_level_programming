-- Script to import table dump and display the top 3 cities with the highest
-- temperature during July and August, ordered by temperature (descending)
SELECT city, temperature
           FROM tablename
           WHERE month IN (7, 8)
           ORDER BY temperature DESC
           LIMIT 3;
