-- SQL script that lists bands with Glam rock as main style, ranked by longevity
-- Column names: band_name and lifespan (in years until 2022)

SELECT band_name, (IFNULL(split, 2022) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;