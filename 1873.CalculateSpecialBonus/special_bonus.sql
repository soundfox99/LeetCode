-- Write your MySQL query statement below

SELECT employee_id, --SELECT normally doesn't end in a , but when you define a case statement it does
CASE
WHEN (MOD(employee_id, 2) = 1) AND (name NOT LIKE 'M%') THEN salary
ELSE 0
END AS bonus --name of last custom column to make for select
FROM Employees
ORDER BY employee_id ASC;