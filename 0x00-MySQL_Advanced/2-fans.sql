-- Ranks country origins, ordered by number of non-unique fans

SELECT origin, SUM(fans) AS nb_fas
FROM metal_bands
GROUP BY origin
ORDER BY nb_fas DESC;