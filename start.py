
from home import Profile 
from home import Home
obj=Profile()
h=Home()

print("\t\t________WELCOME________\n")
choice=int(input("1.Register\n2.Login\n"))
if choice==1:
    obj.register()
elif choice==2:
    obj.login()

