#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 19:11:21 2021

@author: victoria_rodriguez
"""


##Step 1 : Import any needed packages 
 
import pandas as pd 
import sqlalchemy
from sqlalchemy import create_engine
!pip install pymysql

##Step 2 : Connect to SQL 

MYSQL_HOSTNAME = '20.62.193.224'
MYSQL_USER = 'INSERT HERE'
MYSQL_PASSWORD = 'INSERT HERE'
MYSQL_DATABASE = 'ahi'

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}:3305/{MYSQL_DATABASE}'
engine = create_engine(connection_string)

TABLENAME = MYSQL_USER + 'proceduregrouper'

proceduregrouper.to_sql(TABLENAME, con=engine)

##Step 3 : Create a table within the ahi schema 

proceduregrouper = CREATE TABLE userprocedurecostgrouper 
(id INT AUTO_INCREMENT PRIMARY KEY,
patientUID INT NOT NULL,
lastname VARCHAR(50) NOT NULL,
firstname VARCHAR(50) NOT NULL,
SystolicBloodPressure INT NOT NULL
procedure_code INT NOT NULL,
procedure_cost INT NOT NULL),;

##Table can also be created manually and forwarded to SQL schema (See attached Google Collab document for code)

proceduregrouper = pd.DataFrame ({'Patient ID' : ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888'], 
                                                    'Last Name' : ['Roberts', 'Gonzalez', 'McMillin', 'Silva', 'Anthony', 'Washington', 'Martinez', 'Rodriguez'], 
                                                    'First Name' : ['Veronica', 'Jacqueline', 'Miranda', 'Joshua', 'Xavier', 'Mike', 'Jennifer', 'Allen'], 
                                                    'SystolicBloodPressure':['121', '120.5', '140', '131', '138.7', '119', '142', '118'],
                                                    'Procedure Code': ['169553002', '117015009', '301807007', '430193006', '288086009', '76601001', '5880005', '11466000'], 
                                                    'Procedure Cost' : ['14896.56', '2070.44', '12914.35', '416.69', '11354.55', '3001.57', '516.65', '612.34']})

TABLENAME = MYSQL_USER + 'proceduregrouper'

proceduregrouper.to_sql(TABLENAME, con=engine)

##Step 4 : Create trigger within newly created table 

DELIMITER $$
CREATE TRIGGER systolic BEFORE INSERT ON userproceduregrouper
FOR EACH ROW 
BEGIN
    IF NEW.SystolicBloodPressure >= 120 THEN 
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'ERROR: Systolic blood pressure must be 120 mm Hg or below for procedure!';
    END IF; 
END; $$

##Step 5 : Create function within newly created table 

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
END; $$

  
