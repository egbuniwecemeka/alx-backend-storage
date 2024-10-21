-- SQL script that creates a stored procedure AddBonus, 
    -- adding a new correction for a student

-- Set a delimiter
DELIMITER $$

-- Stored procedure
CREATE PROCEDURE AddBonus(
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score INT
)
BEGIN
    DECLARE project_id INT;

    -- Check project existence in projects table
    SELECT id INTO project_id
    FROM projects
    WHERE name = project_name
    LIMIT 1;

-- If project is non-existent, insert it and get new project_id
IF project_id IS NULL THEN
    INSERT INTO projects (name) VALUES (project_name);
    SET project_id = LAST_INSERT_ID();
END IF;

-- Insert correction into the corrections table
INSERT INTO corrections (user_id, project_id, score)
VALUES (user_id, project_name, score);

END $$

-- Restore default delimiter
DELIMITER ;