SELECT subjects.name AS course_name
FROM students
JOIN groups ON students.group_id = groups.id
JOIN subjects ON groups.id = subjects.id
WHERE students.id = 10;