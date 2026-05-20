SELECT timestamp, pm25
FROM air_quality
ORDER BY pm25 DESC
LIMIT 10;
-- Top 10 highest PM2.5 readings