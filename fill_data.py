from faker import Faker
import sqlite3
from sqlite3 import DatabaseError
import logging
from random import randint, sample
import random

NUM_STUDENTS = 40
NUM_GROUPS = 3
NUM_SUBJECTS = 8
NUM_TEACHERS = 4
MAX_GRADES_PER_STUDENT = 20

fake = Faker(['uk_UA'])


def fill_data():
	conn = sqlite3.connect('./db/progress.db')
	cur = conn.cursor()

	for i in range(1, NUM_GROUPS + 1):
		cur.execute('''INSERT INTO groups (id, name) VALUES (?, ?)''', (i, fake.word()))


	for i in range(1, NUM_TEACHERS + 1):
		cur.execute('''INSERT INTO teachers (id, fullname) VALUES (?, ?)''', (i, fake.name()))


	for i in range(1, NUM_SUBJECTS + 1):
		cur.execute('''INSERT INTO subjects (id, name, teacher_id) VALUES (?, ?, ?)''',
		            (i, fake.word(), fake.random_int(min=1, max=NUM_TEACHERS)))


	for i in range(1, NUM_STUDENTS + 1):
		cur.execute('''INSERT INTO students (id, fullname, group_id) VALUES (?, ?, ?)''',
		            (i, fake.name(), fake.random_int(min=1, max=NUM_GROUPS)))


	for student_id in range(1, NUM_STUDENTS + 1):
		subjects = range(1, NUM_SUBJECTS + 1)
		grades = []
		for _ in range(randint(1, MAX_GRADES_PER_STUDENT)):
			subject_id = sample(subjects, 1)[0]
			grade = random.randint(0, 100)
			grade_date = fake.date_between(start_date='-1y', end_date='today')
			cur.execute('''INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (?, ?, ?, ?)''',
			            (student_id, subject_id, grade, grade_date))
			grades.append(subject_id)

	try:
		conn.commit()
	except DatabaseError as e:
		logging.error(e)
		conn.rollback()
	finally:
		cur.close()
		conn.close()
