INSERT INTO students (id, name, age, department, grade) VALUES
(1, 'Akhil', 21, 'Computer Science', 88),
(2, 'Meera', 19, 'Physics', 92),
(3, 'Rohit', 22, 'Mathematics', 75),
(4, 'Sneha', 20, 'Computer Science', 90);
SELECT * FROM students
WHERE age > 20;
SELECT * FROM students
WHERE department IN ('Computer Science', 'Physics');
SELECT * FROM students
WHERE grade = 90;
SELECT * FROM students
WHERE grade BETWEEN 70 AND 90;