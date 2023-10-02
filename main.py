import mysql.connector as connector

class DBhelper:
    def __init__(self):
        self.con=connector.connect(host='localhost',port='3306',password='root',database='pythontest')
        query='create table if not exits user(userID int primary key,username varchar(200),phone varchar(12))'
        cur=self.con.cursor()
        cur.execute(query)

    #insert 
    def insert_user(self,userid,username,phone):
        query="insert into user(userId,userName,phone)values({},'{}','{}')".format(userid,username,phone)
        cur=self.con.cursor()
        cur.excute(query)
        cur.commit()

#main coding
helper=DBhelper()
helper.insert_user()
