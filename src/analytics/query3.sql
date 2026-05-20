SELECT
   DATE_TRUNC('month', timestamp) AS month,
   AVG(pm25) AS avg_pm25
FROM air_quality
GROUP BY month
ORDER BY month;
-- monthly trend