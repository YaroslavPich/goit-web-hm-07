SELECT s.fullname AS student_name, g.grade, g.grade_date
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON g.subject_id = sub.id
JOIN groups gr ON s.group_id = gr.id
WHERE gr.id = 1 AND sub.id = 1;