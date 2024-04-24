import create_db
import logging
import fill_data

logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
	logging.info('Welcome to the student database')
	create_db.create_db()
	fill_data.fill_data()

