import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='Abishek',passwd='1234',database='book_list')
mycursor = mydb.cursor()
l=[]
usr_name='Abishek'
bk1='The kite runner'
sql='select Book_ID from books where Book_name=%s'
mycursor.execute(sql,bk1)
issued=mycursor.fetchone()
for i in issued:
    l.append(i)
cursor=mydb.cursor()
ql='select Book_name from books where Book_name=%s'
cursor.execute(ql,bk1)
issue=cursor.fetchone()
for i in issue:
    l.append(i)
curs=mydb.cursor()
sq='select Author from books where Book_name=%s'
curs.execute(sq,bk1)
iss=curs.fetchone()
for i in iss:
    l.append(i)
l.append(usr_name)
print(l)
query='insert into issued_sample (Book_ID,Book_name,Author,Username) values(%s,%s,%s,%s)'
cursor=mydb.cursor()
cursor.execute(query,l)
mydb.commit()
