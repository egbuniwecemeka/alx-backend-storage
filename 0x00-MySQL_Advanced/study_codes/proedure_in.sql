-- An sql script that creates a procedure with an IN parameter

-- Pick a delimiter
DELIMITER $$

CREATE PROCEDURE proc_in(IN var1 INT)
BEGIN
    SELECT * FROM metal_bands LIMIT var1;
END $$

DELIMITER ;