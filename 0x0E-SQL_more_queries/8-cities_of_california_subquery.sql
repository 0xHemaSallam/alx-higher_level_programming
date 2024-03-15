-- 8-cities_of_california_subquery.sql

SELECT cities
FROM hbtn_0d_usa    
WHERE cities.state_id = states.id
AND states.name = 'California'
ORDER BY cities.id ASC;
