# Write your MySQL query statement below
-- Aproach 2
SELECT DISTINCT email FROM (
    SELECT email,
       row_number() over(partition by email) as rn
    FROM person
) a
where a.rn = 2;


-- Aproach 1
SELECT DISTINCT email FROM person
GROUP BY email
HAVING COUNT(email) > 1;