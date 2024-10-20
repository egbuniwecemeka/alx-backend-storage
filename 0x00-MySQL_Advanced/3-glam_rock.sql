-- Lists all bands with Glam rock as . ranking them by their longevity

SELECT
    band_name
        WHEN split IS NULL THEN 2022 - formed
        ELSE split - formed
    END AS lifespan
FROM
   metal_bands
WHERE
    style = 'Glam rock'
GROUP BY band_name
ORDER BY lifespan DESC;