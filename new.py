from datetime import date
import datetime
#x=datetime.datetime.now()+datetime.timedelta(days=14)
#y=datetime.datetime.now()
d,m,y=('02/17/23').split('/')
int(d)
int(m)
int(y)
x=datetime.datetime.now()
due=datetime.date(d,m,y)
if due<x.strftime("%x"):
    print('True')
else:
    print('False')
#if((z)>14):
    #count=count+1
#print(count)