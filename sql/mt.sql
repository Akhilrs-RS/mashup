INSERT INTO Employee (id, Name, Department, Leaves) VALUES
(1, 'Raju', 'Sales', 1),
(2, 'Sangeetha', 'Sales', 3),
(3, 'Vinay', 'Operations', 8),
(4, 'Abey', 'Packing', 2),
(5, 'Thomas', 'Packing', 1),
(6, 'Muneer', 'Operations', 7),
(7, 'Aparna', 'Sales', 3),
(8, 'Abid', 'Operations', 9),
(9, 'Fathima', 'Sales', 11),
(10, 'Varghese', 'Operations', 14);
INSERT INTO Exam (id, Employee_id, exam_status) VALUES
(1, 2, 'Pass'),
(2, 5, 'Fail'),
(3, 1, 'Fail'),
(4, 8, 'Pass'),
(5, 3, 'Pass'),
(6, 1, 'Pass'),
(7, 6, 'Fail'),
(8, 9, 'Pass'),
(9, 10, 'Pass');
SELECT Name
FROM Employee
WHERE Department = 'Sales' AND Leaves > 5;
SELECT COUNT(*) AS "operations_count"
From Employee
WHERE Department = 'Operations';
SELECT Department, COUNT(Department) AS "employee_count"
FROM Employee
GROUP BY Department;
SELECT Department
FROM Employee
GROUP BY Department
HAVING SUM(Leaves) > 10;
SELECT Employee.Name
FROM Employee
JOIN Exam ON Employee.id = Exam.Employee_id
WHERE Exam.exam_status = 'pass';
SELECT Employee.Name
FROM Employee
LEFT JOIN Exam
ON Employee.id = Exam.Employee_id
WHERE Exam.exam_status IS NULL;

ALTER TABLE Exam ADD FOREIGN KEY (Employee_id) REFERENCES Employee(id);
