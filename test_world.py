import pytest
import mysql.connector
import db_credentials

mydb = mysql.connector.connect(
host=db_credentials.host,
user=db_credentials.user,
passwd=db_credentials.passwd,
database=db_credentials.database
) 

sql = "SELECT * FROM fourier_processed_stock LIMIT 0,1"
def read_database(sql):
	mycursor = mydb.cursor()
	mycursor.execute(sql)
	table_rows = mycursor.fetchall()
	return table_rows

#sql2 = "INSERT INTO fourier_processed_stock (date_of_day, label, numberOfTrades, name, volume, fft_20_close, fft_20_open, fft_20_low, fft_20_high, fft_100_close, fft_100_open, fft_100_low, fft_100_high) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#val2 = ('2020-05-22', '09:30 AM', 35, 'TEST', 5594, 164.58, 164.596, 164.527, 164.629, 44.57, 44.675, 44.54, 44.715)

#def insert_to_database(sql,val):
#	mycursor = mydb.cursor()
#	mycursor.execute(sql, val)
#	return "record inserted."


sql = "SELECT * FROM unlabelled_record GROUP BY name ORDER BY date_of_day LIMIT 0,1"
def select_min_from_db_by_stock_name_and_date(sql):
	mycursor = mydb.cursor()
	mycursor.execute(sql)
	table_rows = mycursor.fetchall()
	return table_rows

#def test_read_database():
#	assert(read_database(sql)) == [(1, '2020-05-22', '09:30 AM', 35, 'CSCO', 5594, 164.58, 164.596, 164.527, 164.629, 44.57, 44.675, 44.54, 44.715)]

#def test_insert_database():
#	assert(insert_to_database(sql2,val2)) == "record inserted."

print(select_min_from_db_by-_stock_name_and_date(sql))