import sqlite3


def create_db():
	with open('success.sql', 'r') as f:
		sql = f.read()

	with sqlite3.connect('db/progress.db') as con:
		cur = con.cursor()
		cur.executescript(sql)


if __name__ == "__main__":
	pass
