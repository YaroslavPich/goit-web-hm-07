import sqlite3

import create_db
import logging
import fill_data

logging.basicConfig(level=logging.DEBUG)


def request(number):
	with open(f'./select/query_{number}.sql', 'r') as f:
		sql = f.read()
	return sql


def execute_query(sql):
	with sqlite3.connect('./db/progress.db') as con:
		cur = con.cursor()
		cur.execute(sql)
		return cur.fetchall()


if __name__ == '__main__':
	print('''   Ласкаво просимо до бази даних успішності студентів!
1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
2. Знайти студента із найвищим середнім балом з певного предмета.
3. Знайти середній бал у групах з певного предмета.
4.Знайти середній бал на потоці (по всій таблиці оцінок).
5. Знайти які курси читає певний викладач.
6. Знайти список студентів у певній групі.
7. Знайти оцінки студентів у окремій групі з певного предмета.
8. Знайти середній бал, який ставить певний викладач зі своїх предметів.
9. Знайти список курсів, які відвідує студент.
10. Список курсів, які певному студенту читає певний викладач.
11. Середній бал, який певний викладач ставить певному студентові.
12. Оцінки студентів у певній групі з певного предмета на останньому занятті.''')
	print('Для того щоб продовжити виберіть цифрою номер запиту. Або введіть "Вихід"')
	create_db.create_db()
	fill_data.fill_data()
	while True:
		while True:
			user_input = input("Виберіть команду запиту: ")
			if user_input:
				break
			else:
				print("Ви нічого не ввели")
		command = user_input

		if command in ("Вихід"):
			print("Допобачення!")
			break
		elif command == '1':
			print(execute_query(request(1)))
		elif command == '2':
			print(execute_query(request(2)))
		elif command == '3':
			print(execute_query(request(3)))
		elif command == '4':
			print(execute_query(request(4)))
		elif command == '5':
			print(execute_query(request(5)))
		elif command == '6':
			print(execute_query(request(6)))
		elif command == '7':
			print(execute_query(request(7)))
		elif command == '8':
			print(execute_query(request(8)))
		elif command == '9':
			print(execute_query(request(9)))
		elif command == '10':
			print(execute_query(request(10)))
		elif command == '11':
			print(execute_query(request(11)))
		elif command == '12':
			print(execute_query(request(12)))
		else:
			print("Invalid command.")
