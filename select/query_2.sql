SELECT s.fullname AS student_name, AVG(g.grade) AS average_grade, sub.name AS subject
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON g.subject_id = sub.id
WHERE sub.id = 1
GROUP BY s.id
ORDER BY average_grade DESC
LIMIT 1;