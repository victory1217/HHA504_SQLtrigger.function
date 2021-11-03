##TRIGGER FOR ahi.victoriarodriguezsilvaproceduregrouper
DELIMITER $$
CREATE TRIGGER systolic BEFORE INSERT ON victoriarodriguezsilvaproceduregrouper
FOR EACH ROW 
BEGIN
    IF NEW.SystolicBloodPressure >= 120 THEN 
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'ERROR: Systolic blood pressure must be 120 mm Hg or below for procedure!';
    END IF; 
END; $$

##FUNCTION FOR ahi.victoriarodriguezsilvaproceduregrouper
DELIMITER $$
CREATE FUNCTION ProcedureCost(
    cost DECIMAL(10,2)
)

RETURNS VARCHAR(20)
DETERMINISTIC
BEGIN
DECLARE procedureCost VARCHAR(20);
IF cost > 10000 THEN
SET procedureCost = ‘expensive’;

ELSEIF (cost >= 1000 AND
credit <= 5000) THEN
SET procedureCost = 'standard';

ELSEIF cost < 1000 THEN
SET procedureCost = 'cheap';
END IF;
-- return the procedure cost category
RETURN (procedureCost);
END$$
DELIMITER ;


