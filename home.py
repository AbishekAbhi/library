import csv
import datetime
from user_profile import Profile
import mysql.connector
class Home:
    
    def __init__(self) -> None:
        pass
    def home(self,usr_name):
        print("\t\t________HOME________\n")
        opt=int(input("1.Search bar\n2.Checkout(s)\n3.Sign out\n"))
        if opt==1:
            h.search(usr_name)
        elif opt==2:
            h.checkout(usr_name)
        elif opt==3:
            exit()
            

    def search(self,usr_name):
        global bk
        print("\t\t________SEARCH BAR________\n")
        bk=input("Search-'Book or Author name':\t")
        h.availability(bk,usr_name)
        
    def availability(self,bk_name,usr_name):
        l=[]
        flag=True
        val=True
        data=0
        mydb=mysql.connector.connect(host='localhost',user='Abishek',passwd='1234',database='book_list')
        mycursor = mydb.cursor()
        mycursor.execute('select Book_name from issued')
        issued=mycursor.fetchall()
        for i in issued:
            if bk_name in i:
                val=False 
        if val==True:
            cursor=mydb.cursor()
            sql='select Book_name from books'
            cursor.execute(sql)
            name=cursor.fetchall()
            for i in name:
                if bk_name in i:
                    print('Available')
                    flag=False
            point=mydb.cursor()
            point.execute('select Author from books')
            author=point.fetchall()
            for j in author:
                if bk_name in j:
                    query='select Book_name from books where Author=%s'
                    result=mydb.cursor()
                    result.execute(query,j)
                    for k in result:
                        print(f'Available:{k}')
                        flag=False
                        data=1
                    break
        if flag == True:
            print("Not Available!!!")
            h.home(usr_name)
        elif data==1:
            h.search(usr_name)
        else:
            h.issue(bk_name,usr_name)
                    
            

    def issue(self,bk1,usr_name):
        l=[]
        bk=[]
        bk.append(bk1)
        choice=input("Do you want to afford it?\n1.Yes\n2.No\n")
        mydb=mysql.connector.connect(host='localhost',user='Abishek',passwd='1234',database='book_list')
        mycursor = mydb.cursor()
        if choice=='1':
            sql='select Book_ID from books where Book_name=%s'
            mycursor.execute(sql,bk)
            issued=mycursor.fetchone()
            for i in issued:
                l.append(i)
            cursor=mydb.cursor()
            ql='select Book_name from books where Book_name=%s'
            cursor.execute(ql,bk)
            issue=cursor.fetchone()
            for i in issue:
                l.append(i)
            curs=mydb.cursor()
            sq='select Author from books where Book_name=%s'
            curs.execute(sq,bk)
            iss=curs.fetchone()
            for i in iss:
                l.append(i)
            l.append(usr_name)
            query='insert into issued (Book_ID,Book_name,Author,Username,Issued_date,Due_date) values(%s,%s,%s,%s,CURDATE(),CURDATE()+15)'
            cursor=mydb.cursor()
            cursor.execute(query,l)
            mydb.commit()
            print("Your book is issued.")
            h.home(usr_name)
        elif choice=='2':
            h.home(usr_name)
    def checkout(self,usr_name):
        l=[]
        l.append(usr_name)
        mydb=mysql.connector.connect(host='localhost',user='Abishek',passwd='1234',database='book_list')
        mycursor = mydb.cursor()
        query='select * from issued where Username=%s'
        mycursor.execute(query,l)
        result=mycursor.fetchall()
        for i in result:
            print(i)
        h.home(usr_name)        
                    
                    
obj1=Profile()   
h=Home()




           