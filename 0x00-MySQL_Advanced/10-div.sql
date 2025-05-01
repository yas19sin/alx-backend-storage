-- SQL script that creates a function SafeDiv that divides two numbers safely
-- Returns a / b or 0 if b == 0
-- Function takes 2 arguments: a (INT), b (INT)

DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT) 
RETURNS FLOAT
DETERMINISTIC
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END$$
DELIMITER ;