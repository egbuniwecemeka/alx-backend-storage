-- An sql script that creates a trigger that decreases the quantity of an item after adding a new item

CREATE TRIGGER dec_quant
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    -- Updates the quantity in the items table based on the order
    UPDATE items
    SET quantity = quantity - NEW.number