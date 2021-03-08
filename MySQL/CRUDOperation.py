import mysql.connector #Importing Connector package

mysqldb=mysql.connector.connect(host="localhost",user="root",password="mundhe012@")#established connection

mycursor=mysqldb.cursor()#cursor() method create a cursor object

mycursor.execute("use dbpython")#Execute SQL Query to create a database

#mycursor.execute("create table Test(roll INT,name VARCHAR(255), marks INT)")#Execute SQL Query to create a table into your database

try:
   #Execute SQL Query to insert record
   mycursor.execute("insert into Test values(1,'Sarfaraj',80),(2,'Kumar',89),(3,'Sohan',90)")
   mysqldb.commit() # Commit is used for your changes in the database
   print('Record inserted successfully...')
except:
   # rollback used for if any error
   mysqldb.rollback()
try:
   mycursor.execute("select * from Test")#Execute SQL Query to select all record
   result=mycursor.fetchall() #fetches all the rows in a result set
   for i in result:
      roll=i[0]
      name=i[1]
      marks=i[2]
      print(roll,name,marks)
except:
   print('Error:Unable to fetch data.')


try:
   mycursor.execute("UPDATE Test SET name='Ramu', marks=100 WHERE roll=1")#Execute SQL Query to update record
   mysqldb.commit() # Commit is used for your changes in the database
   print('Record updated successfully...')
except:
   # rollback used for if any error
   mysqldb.rollback()


try:
   mycursor.execute("DELETE FROM Test WHERE roll=3")#Execute SQL Query to detete a record
   mysqldb.commit() # Commit is used for your changes in the database
   print('Record deleted successfully...')
except:
   # rollback used for if any error
   mysqldb.rollback()
mysqldb.close()#Connection Close




