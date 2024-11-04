-- Question 1: Query to display 2020 data ordered by driver points
SELECT driver_id, driver_name, team, driver_points
FROM driver_standings
WHERE race_year = 2020
ORDER BY driver_points DESC;
