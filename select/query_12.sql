SELECT students.fullname AS student_name, grades.grade, grades.grade_date
FROM students
JOIN groups ON students.group_id = groups.id
JOIN subjects ON groups.id = subjects.id
JOIN grades ON students.id = grades.student_id
WHERE groups.id = 2 AND subjects.id = 2
      AND grades.grade_date = (SELECT MAX(grade_date) FROM grades WHERE subject_id = 2);