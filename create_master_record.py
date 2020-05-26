import pandas as pd
import itertools
import os
import utils
import mysql.connector
import db_credentials

def main():
    pass


if __name__ == "__main__":

	mydb = mysql.connector.connect(
	  host=db_credentials.host,
	  user=db_credentials.user,
	  passwd=db_credentials.passwd,
	  database=db_credentials.database
	) 

	sql = "SELECT name, MIN(fft_100_close) FROM unlabelled_record GROUP BY name"
	table_rows = utils.extract_data(sql)
	min_index_list = []
	i = 0
	while i < len(table_rows):
		sql = "SELECT id FROM unlabelled_record WHERE name = '"+str(table_rows[i][0])+"' AND fft_100_close LIKE "+str(table_rows[i][1]).replace('.0','')
		utils.get_index(sql,min_index_list)
		i += 1

	sql = "SELECT name, MAX(fft_100_close) FROM unlabelled_record GROUP BY name"
	table_rows = utils.extract_data(sql)
	max_index_list = []
	i = 0
	while i < len(table_rows):
		sql = "SELECT id FROM unlabelled_record WHERE name = '"+str(table_rows[i][0])+"' AND fft_100_close LIKE "+str(table_rows[i][1]).replace('.0','')
		utils.get_index(sql,max_index_list)
		i += 1

	sql = "SELECT * FROM unlabelled_record"
	table_rows = utils.extract_data(sql)
	label = [0]*len(table_rows)
	utils.labelling_data(label)

