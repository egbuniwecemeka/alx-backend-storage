-- SQL script creating a trigger that resets the valid_email attribute
    -- only when the email nas been changed.
DELIMITER $$

-- Create Trigger that resets the valid_email on every email change
CREATE TRIGGER reset_email
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        -- Update valid_email field for the specific user
        UPDATE users
        SET valid_email = 0
        WHERE id = NEW.id;
    END IF;
END $$