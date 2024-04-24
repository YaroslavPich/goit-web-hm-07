SELECT subjects.name AS course_name
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
JOIN teachers ON subjects.teacher_id = teachers.id
JOIN groups ON students.group_id = groups.id
WHERE students.id = 1 AND teachers.id = 2;