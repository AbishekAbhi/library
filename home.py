import datetime
from user_profile import Profile
class Home:
    
    def __init__(self) -> None:
        pass
    def home(self):
        print("\t\t________HOME________\n")
        opt=int(input("1.Search bar\n2.Sign out\n"))
        if opt==1:
            h.search()
        elif opt==2:
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
           h.checkout(issued)
           
        elif choice=='2':
            h.home()
    def checkout(self,books):
        print("\t\t________Checkout(s)________\n")
        key=[]
        value=[]
        for i in books:
            key.append(i)
            value.append(books[i])
        issue_date=datetime.datetime.now()
        due_date=datetime.datetime.now()+datetime.timedelta(days=14)
        print(f'Book ID:{key}\tBook Name:{value}\nIssued date:{issue_date.strftime("%x")}\nDue date:{due_date.strftime("%x")}')
        h.home()        
                    
                    
obj1=Profile()   
h=Home()




           