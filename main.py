from time import strftime, strptime
import pywhatkit as kit
import datetime
phoneNumber=str(input())
messageText='Phone number'

t=datetime.datetime.now()
m=t.minute+1
print(t.hour,":",m)
kit.sendwhatmsg(phoneNumber, messageText, t.hour,m)

