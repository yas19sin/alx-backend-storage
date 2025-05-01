-- SQL script that creates a view need_meeting listing students who need a meeting
-- Students with score under 80 (strict) and no last_meeting or more than 1 month ago

CREATE VIEW need_meeting AS
SELECT name 
FROM students 
WHERE score < 80 
AND (last_meeting IS NULL OR last_meeting < DATE_SUB(CURRENT_DATE(), INTERVAL 1 MONTH));