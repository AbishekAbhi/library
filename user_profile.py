
class Profile:


    def __init__(self) -> None:
        pass
    def register(self):
        from validation import Validate
        obj3=Validate()
        print("\t\t________REGISTER________\n")
        credentials={}
        name=(input("Username:\t"))
        password=(input("Password:\t"))
        obj3.validate(password)
        credentials[name]=password  
        obj1.login(credentials)
    def login(self,data):
        from home import Home
        obj2=Home() 
        print("\t\t________LOGIN________\n")
        var=1
        while var==1:
            global usr_name
            usr_name=input("Username:\t")
            if usr_name in data :
                pass_word=input("Password:\t")
                if data[usr_name]==pass_word:
                    print("Successfully logged in!!")
                    var=0
                    obj2.home()
                else:
                    print("Incorrect password!!\n Enter valid Password.")
            else:
                print("Incorrect username !!\n Enter valid Username.")

obj1=Profile()
