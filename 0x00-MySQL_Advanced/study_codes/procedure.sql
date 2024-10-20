-- Pick a delimiter
DELIMITER $$

-- Creating a procedure that displays data from metal_bands table
CREATE PROCEDURE style_fans()
    BEGIN
        SELECT style, SUM(fans) AS total_fans
        FROM metal_bands
        GROUP BY style
        ORDER BY total_fans DESC;
    END $$

DELIMITER ;

-- Call the procedure
CALL style_fans()