# Write your MySQL query statement below
SELECT a.Employee FROM (
    SELECT e.id, e.name as Employee, e.salary as Employee_Sal, 
       e.managerId, m.name, m.salary
    FROM Employee e INNER JOIN Employee m
    ON e.managerId = m.id
    WHERE e.salary > m.salary
) a

