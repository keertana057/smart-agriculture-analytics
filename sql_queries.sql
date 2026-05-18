-- TOP PRODUCING CROPS

SELECT crop,
SUM(production) AS total_production
FROM crop_production
GROUP BY crop
ORDER BY total_production DESC
LIMIT 10;


-- TOP PRODUCING STATES

SELECT state,
SUM(production) AS total_production
FROM crop_production
GROUP BY state
ORDER BY total_production DESC;


-- SEASONAL PRODUCTION ANALYSIS

SELECT season,
SUM(production) AS total_production
FROM crop_production
GROUP BY season
ORDER BY total_production DESC;


-- YEAR-WISE PRODUCTION TREND

SELECT year,
SUM(production) AS total_production
FROM crop_production
GROUP BY year
ORDER BY year;


-- TOP DISTRICTS BY PRODUCTION

SELECT district,
SUM(production) AS total_production
FROM crop_production
GROUP BY district
ORDER BY total_production DESC
LIMIT 10;


-- AVERAGE RAINFALL BY AREA

SELECT area,
AVG(average_rain_fall_mm_per_year)
AS avg_rainfall
FROM rainfall
WHERE average_rain_fall_mm_per_year IS NOT NULL
GROUP BY area
ORDER BY avg_rainfall DESC;


-- HIGHEST YIELD CROPS

SELECT item,
AVG(value) AS avg_yield
FROM yield_data
GROUP BY item
ORDER BY avg_yield DESC
LIMIT 10;


-- RAINFALL VS YIELD ANALYSIS

SELECT y.area,
AVG(r.average_rain_fall_mm_per_year)
AS rainfall,
AVG(y.value) AS yield_value
FROM yield_data y
JOIN rainfall r
ON y.area = r.area
WHERE r.average_rain_fall_mm_per_year IS NOT NULL
GROUP BY y.area;


-- TOTAL AGRICULTURAL PRODUCTION

SELECT SUM(production)
AS total_agriculture_production
FROM crop_production;


-- TOTAL CULTIVATED AREA

SELECT SUM(area)
AS total_cultivated_area
FROM crop_production;


-- NUMBER OF UNIQUE CROPS

SELECT COUNT(DISTINCT crop)
AS total_crops
FROM crop_production;


-- NUMBER OF STATES

SELECT COUNT(DISTINCT state)
AS total_states
FROM crop_production;


-- AVERAGE PRODUCTION BY CROP

SELECT crop,
AVG(production) AS avg_production
FROM crop_production
GROUP BY crop
ORDER BY avg_production DESC;


-- LOWEST RAINFALL AREAS

SELECT area,
AVG(average_rain_fall_mm_per_year)
AS avg_rainfall
FROM rainfall
WHERE average_rain_fall_mm_per_year IS NOT NULL
GROUP BY area
ORDER BY avg_rainfall ASC
LIMIT 10;


-- HIGHEST PRODUCTION YEAR

SELECT year,
SUM(production) AS total_production
FROM crop_production
GROUP BY year
ORDER BY total_production DESC
LIMIT 1;


-- CREATE TOP CROP SUMMARY VIEW

CREATE VIEW top_crop_summary AS
SELECT crop,
SUM(production) AS total_production
FROM crop_production
GROUP BY crop;


-- CREATE STATE PRODUCTION SUMMARY VIEW

CREATE VIEW state_production_summary AS
SELECT state,
SUM(production) AS total_production
FROM crop_production
GROUP BY state;


-- CREATE RAINFALL SUMMARY VIEW

CREATE VIEW rainfall_summary AS
SELECT area,
AVG(average_rain_fall_mm_per_year)
AS avg_rainfall
FROM rainfall
WHERE average_rain_fall_mm_per_year IS NOT NULL
GROUP BY area;