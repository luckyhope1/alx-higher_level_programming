-- Script to import table dump and display the maximum temperature of each
-- state, ordered by state name
SELECT state, MAX(temperature) AS max_temperature
           FROM tablename
           GROUP BY state
           ORDER BY state;
