--Script that creates a function `SafeDiv` 
--that divides (and returns) the first by the second number
--or returns 0 if the second number is equal to 0
DELIMITER |
DROP FUNCTION IF EXISTS SafeDiv;
CREATE FUNCTION SafeDiv (x INT, y INT)
RETURNS FLOAT
BEGIN
  DECLARE result FLOAT;
  IF y = 0 THEN
    SET result = 0;
  ELSE
    SET result = x / y;
  END IF;
  RETURN result;
END;
|