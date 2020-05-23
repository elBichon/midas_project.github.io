import mysql.connector

#create database
#mydb = mysql.connector.connect(
#    host = "localhost",
#    user = "newuser",
#    passwd = "password"
#)

#print('creating database for Midas Hand')
#mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE Midas_Hand")
#mycursor.execute("SHOW DATABASES")

#for x in mycursor:
#  print(x) 
#connect to database
mydb = mysql.connector.connect(
  host="localhost",
  user="newuser",
  passwd="password",
  database="Midas_Hand"
) 


mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE raw_stock (id INT AUTO_INCREMENT PRIMARY KEY, date_of_day VARCHAR(255), complete_date VARCHAR(255), high FLOAT, low FLOAT, open FLOAT, close FLOAT)") 

#mycursor.execute("ALTER TABLE raw_stock ADD COLUMN date_of_day VARCHAR(255)")


#sql = "INSERT INTO raw_stock (date_of_day, date, high, low, open, close) VALUES (%s, %s, %s, %s, %s, %s)"
#val = [
 # ('2020-05-12', '2020-05-12 15:59:00', 100,120,12.34,14)
#]

#mycursor.executemany(sql, val)

#mydb.commit()

#print(mycursor.rowcount, "was inserted.")

mycursor.execute("SELECT * FROM raw_stock")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
