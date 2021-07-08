import time
from plyer import notification

while True :
   
   notification.notify(title='**Please Drink water now',message='Get up! Get up! Time to drink water.',app_icon = 'Icon.ico' , timeout=10)
    
   time.sleep(60*60)


#To start the backgroung running commands
#python3 Drinkingwatertimer.py &

#To kill the background running commands
#kill -9 {{id got after }} &

#For flushing 
#python3 filename.py > filenameToFlush &
