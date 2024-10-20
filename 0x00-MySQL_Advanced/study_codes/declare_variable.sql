-- A scrpit that declares local variables in a BEGIN/END block stored procedure

-- Set the delimiter
DELIMITER $$

-- Stored Procedure Routine that demonstrates variable declaration and scope
CREATE PROCEDURE my_vars()
    BEGIN
        -- Declare variables a, b, and c
        DECLARE a INT DEFAULT 10;
        DECLARE b, c INT;

        -- Modify variable a and set values for b and c
        SET a = a + 100;
        SET b = 2;
        SET c = a + b;

        -- Inner block that declares local variable c (scoped to block)
        BEGIN
            DECLARE c INT;
            SET c = 5;
            SELECT a, b, c;
        END;
        SELECT a, b, c;
    END $$

    -- Restore the delimiter
    DELIMITER ;