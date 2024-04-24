SELECT s.group_id AS group_id, sub.name AS subject_name, AVG(g.grade) AS average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON g.subject_id = sub.id
WHERE sub.id = 1
GROUP BY s.group_id, sub.name;