import csv
import datetime
from user_profile import Profile
class Home:
    
    def __init__(self) -> None:
        pass
    def home(self):
        print("\t\t________HOME________\n")
        opt=int(input("1.Search bar\n2.Checkout(s)\n3.Sign out\n"))
        if opt==1:
            h.search()
        elif opt==2:
            h.checkout()
        elif opt==3:
            exit()
            

    def search(self):
        
        print("\t\t________SEARCH BAR________\n")
        book_det={'101':'The push','102':'Room on the roof','103':'Girl you left behind','104':'The man called owe','105':'The kite runner','106':'A thousand splendid suns'}
        print(f'{book_det}\n')
        bk=input("Search-'Book Id':\t")
        if bk in book_det:
            print("Available!!!")
            h.issue(bk,book_det)
        else:
            print("Not available!!")

    def issue(self,bk,book_det):
        choice=input("Do you want to afford it?\n1.Yes\n2.No\n")
        if choice=='1':
           issued={}
           issued[bk]=book_det[bk]
           print("Your book is issued")
           
        elif choice=='2':
            h.home()
    def checkout(self,usr_name):
        with open('issued_list.csv','r') as file:
            data=csv.reader(file)
            for line in data:
                if (line[3]==usr_name):
                    print(f'Id:{line[0]}\nBook name:{line[1]}--{line[2]}\nIssued date:{line[4]}\nDue date:{line[5]}')
        h.home(usr_name)        
                    
                    
obj1=Profile()   
h=Home()




           