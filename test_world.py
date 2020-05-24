import pytest
import mysql.connector
import db_credentials

mydb = mysql.connector.connect(
host=db_credentials.host,
user=db_credentials.user,
passwd=db_credentials.passwd,
database=db_credentials.database
) 

def read_database(sql):
	try:
		mycursor = mydb.cursor()
		mycursor.execute(sql)
		table_rows = mycursor.fetchall()
	except:
		pass
	return table_rows

def insert_to_database(sql,val):
	try:
		mycursor = mydb.cursor()
		mycursor.execute(sql, val)
	except:
		pass
	return "record inserted."

def insert_multiple_into_db(sql,val):
	i = 0
	while i < 1:
		try:
			mycursor = mydb.cursor()
			mycursor.execute(sql, val)
			print(mycursor.rowcount, "record inserted.")
		except:
			print('insertion failed')
			pass
		i += 1
	mydb.commit()
	return "record inserted."

def select_min_from_db(sql_get_min_max,sql_get_id):
	try:
		mycursor = mydb.cursor()
		mycursor.execute(sql_get_min_max)
		table_rows = mycursor.fetchall()[0][0]
		sql = sql_get_id + str(table_rows)
	except:
		pass
	try:
		mycursor.execute(sql)
		table_rows = mycursor.fetchall()[0][0]
	except:
		pass
	return table_rows


def test_read_database():
	assert(read_database(sql)) == [(1, '2020-05-22', '09:30 AM', 'CSCO', 44.715, 44.54, 44.675, 44.57, 5594, 35)]

def test_insert_database():
	assert(insert_to_database(sql2,val2)) == "record inserted."

def test_get_min():
	assert(select_min_from_db(sql_get_min_max,sql_get_id)) == 144

def test_insert_multiple_into_db():
	assert(insert_multiple_into_db(sql,val)) == "record inserted."

sql_insert = "INSERT INTO raw_stock (date, label, name, high, low, open, close, volume, numberOfTrades) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = ('20-05-22','3:55 PM', 'TEST',44.900,44.870,44.875,44.89,70,88)
sql = "SELECT * FROM raw_stock LIMIT 0,1"
sql2 = "INSERT INTO fourier_processed_stock (date_of_day, label, numberOfTrades, name, volume, fft_20_close, fft_20_open, fft_20_low, fft_20_high, fft_100_close, fft_100_open, fft_100_low, fft_100_high) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val2 = ('2020-05-22', '09:30 AM', 35, 'TEST', 5594, 164.58, 164.596, 164.527, 164.629, 44.57, 44.675, 44.54, 44.715)
sql_get_min_max = "SELECT MIN(fft_100_close) FROM unlabelled_record GROUP BY name ORDER BY date_of_day"
sql_get_id = "SELECT id FROM unlabelled_record WHERE fft_100_close LIKE "
test_read_database()
test_insert_database()
test_get_min()
test_insert_multiple_into_db()