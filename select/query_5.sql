SELECT s.name AS course
FROM subjects s
JOIN teachers t ON s.teacher_id = t.id
WHERE t.id = 3;