from faker import Faker
from random import randint
import sqlite3
from sqlite3 import DatabaseError
import logging

fake = Faker()


def fill_data():
	conn = sqlite3.connect('./db/progress.db')
	cur = conn.cursor()
	for _ in range(3):
		cur.execute('INSERT INTO groups (name) VALUES (?)', (fake.word(),))

	for _ in range(3):
		cur.execute('INSERT INTO teachers (fullname) VALUES (?)', (fake.name(),))

	for teacher_id in range(1, 4):
		for i in range(2):
			cur.execute('INSERT INTO subjects (name, teacher_id) VALUES (?, ?)', (fake.word(), teacher_id))

	for group_id in range(1, 4):
		for _ in range(10):
			cur.execute('INSERT INTO students (fullname, group_id) VALUES (?, ?)', (fake.name(), group_id))
			student_id = cur.lastrowid
			for subject_id in range(1, 7):
				for _ in range(3):
					cur.execute('INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (?, ?, ?, ?)',
					            (student_id, subject_id, randint(0, 100), fake.date_this_decade()))

	try:
		conn.commit()
	except DatabaseError as e:
		logging.error(e)
		conn.rollback()
	finally:
		cur.close()
		conn.close()
