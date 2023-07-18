-- Script to import table dump and display average temperature (in Fahrenheit)
-- by city, ordered by temperature (descending)
SELECT city, AVG(temperature) AS average_temperature_fahrenheit
           FROM tablename
           GROUP BY city
           ORDER BY average_temperature_fahrenheit DESC;
