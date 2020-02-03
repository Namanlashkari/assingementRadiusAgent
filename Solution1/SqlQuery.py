import mysql.connector
from mysql.connector import Error
 
try:
    conn = mysql.connector.connect(host='localhost',
                                         database='realestate',
                                         user='root',
                                         password='**********',
                                         auth_plugin='mysql_native_password')

   
    if conn.is_connected():
        db_Info = conn.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
   
    mysqlmySql_Create_Table_Query = CREATE TABLE  properties( 
                                     Id int(11) NOT NULL unique ,
                                     latitude float NOT NULL,
                                     longitute float NOT NULL,
                                     Price float NOT NULL,
                                     bedroom int NOT NULL,
                                     bathroom int NOT NULL,
                                     PRIMARY KEY (Id))
    
    mySql_Retrieve_Table_Query = Select * from properties p where (p.lat between Lat-0.145 and Lat+0.145) and (p.long between Long-0.182 and Long+0.182)
    
    
    
    cursor = conn.cursor()
    result = cursor.execute(mySql_Retrieve_Table_Query)
    print("Data Retrieved")
    
    
    
except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
    
except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if (conn.is_connected()):
        cursor.close()
        conn.close()
        print("MySQL connection is closed")
