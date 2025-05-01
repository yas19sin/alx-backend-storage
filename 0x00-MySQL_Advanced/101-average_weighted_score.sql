-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers
-- Computes and stores the average weighted score for all students

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users AS u
    SET u.average_score = (
        SELECT SUM(c.score * p.weight) / SUM(p.weight)
        FROM corrections AS c
        JOIN projects AS p ON c.project_id = p.id
        WHERE c.user_id = u.id
    );
END$$
DELIMITER ;