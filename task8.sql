UPDATE country_vaccination_stats AS target
SET daily_vaccinations = s.min_value
FROM (
  SELECT country, MIN(daily_vaccinations) AS min_value
  FROM country_vaccination_stats
  WHERE daily_vaccinations IS NOT NULL
  GROUP BY country
) AS s
WHERE target.country = s.country
AND target.daily_vaccinations IS NULL;
