import pandas as pd
import itertools
import os
import utils
import mysql.connector
import db_credentials


def main():
    pass
#connect to the database
#select the data
#rename the columns
#get min (-1) and max(1) or else (0) per company per day
#insert label and the other data in the master record


if __name__ == "__main__":

	mydb = mysql.connector.connect(
	  host=db_credentials.host,
	  user=db_credentials.user,
	  passwd=db_credentials.passwd,
	  database=db_credentials.database
	) 

	#sql = "SELECT INDEX(MIN(fft_100_close)) FROM unlabelled_record GROUP BY name ORDER BY date_of_day"
	def select_min_from_db_by_stock_name_and_date(sql):
		mycursor = mydb.cursor()
		mycursor.execute(sql)
		table_rows = mycursor.fetchall()
		return table_rows



	sql = "SELECT MIN(fft_100_close) FROM unlabelled_record GROUP BY name ORDER BY date_of_day"
	min_value = (select_min_from_db_by_stock_name_and_date(sql))
	print(type(min_value[0][0]))
	sql = "SELECT id FROM unlabelled_record WHERE fft_100_close LIKE "+str(min_value[0][0])
	print(sql)
	print(select_min_from_db_by_stock_name_and_date(sql))
