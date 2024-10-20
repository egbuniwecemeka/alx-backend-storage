-- A script show user variables in a procedure

-- Set a temporal delimiter
DELIMITER $$

-- Create Procedure
CREATE PROCEDURE user_var()
    BEGIN
        DECLARE x, y INT;
        SET @x = 5;
        SET @y = 10;
        SELECT @x, @y, @x - @y; 
    END

DELIMITER ;