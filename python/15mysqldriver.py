import mysql.connector as MyCon

my_db=MyCon.connect(
    host="localhost", 
    user="root",
    password="root",
    database="python" #Give database name If is available in the database
    )

print(my_db, "Connection establish...")

db_cursor = my_db.cursor()
######### Create Database in MySql database
#db_cursor.execute("create database python")
#print("Database has been created")


######### Create Table in MySql database
#db_cursor.execute("create table user(roll int, name varchar(50))")
#print("Table has been created")

######### Show all Tables
# db_cursor.execute("show tables")
# for tables in db_cursor:
#     print(tables)

######### Insert single data in the table
# insert_query = "insert into user(roll, name) values (%s, %s)"
# insert_value = (2, "Ajeet Kushwaha")
# db_cursor.execute(insert_query, insert_value)
# my_db.commit()
#print(db_cursor.rowcount, "Data inserted.....")


######### Insert multiple data in the table
# insert_query = "insert into user(roll, name) values (%s, %s)"
# insert_list = [(5, "abcef"), (6, "abcdefg"), (7, "abcdefgh")]
# db_cursor.executemany(insert_query, insert_list) # executemany used for insert many records
# my_db.commit()
# print(db_cursor.rowcount, "Data inserted.....")


######### Get users data from table
#db_cursor.execute("select * from user") # Get all data
#db_cursor.execute("select * from user where roll=2") # Retrieve data by roll number
# for user in db_cursor:
#     print(user)

######### Update user
# update_query = "update user set name=%s where roll=%s"
# update_value = ("Ajeet Maurya", 2)
# db_cursor.execute(update_query, update_value)
#my_db.commit()
# print(db_cursor.rowcount, "data updated...")


######### Delete user
# delete_query = "delete from user where roll=%s"
# delete_value = (3,)
# db_cursor.execute(delete_query, delete_value)
# my_db.commit()
# print(db_cursor.rowcount, "data delete...")

######### Delete all user data
delete_alldata_query="truncate table user"
db_cursor.execute(delete_alldata_query)
my_db.commit()
print(db_cursor.rowcount, "all data delete...")


db_cursor.execute("select * from user") # Retrieve data by roll number
for user in db_cursor:
    print(user)