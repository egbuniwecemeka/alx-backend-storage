-- An sql script that creates a trigger that decreases the quantity of an item after adding a new order

--Set Delimiter
DELIMITER $$ 

-- Create trigger
CREATE TRIGGER dec_quant
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    -- Updates the quantity in the items table based on the order
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END $$

-- Reset to default delimiter
DELIMITER ;