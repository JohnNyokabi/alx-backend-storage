-- script that creates a stored procedure `ComputeAverageWeightedScoreForUsers`
-- that computes and stores the average weighted score for all students
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER |
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  UPDATE users, 
    (SELECT users.id, SUM(score * weight) / SUM(weight) AS avg_wgt 
    FROM users
    JOIN corrections ON users.id=corrections.user_id 
    JOIN projects ON corrections.project_id=projects.id 
    GROUP BY users.id)
  AS Avg_Weight
  SET users.average_score = Avg_Weight.avg_wgt
  WHERE users.id=Avg_Weight.id;
END;
|