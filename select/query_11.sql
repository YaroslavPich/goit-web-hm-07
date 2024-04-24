SELECT AVG(grades.grade) AS average_grade
FROM grades
JOIN students ON grades.student_id = students.id
JOIN subjects ON grades.subject_id = subjects.id
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE students.id = 11 AND teachers.id = 2;