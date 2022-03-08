import os 
import time 

os.system('color a')

while True:
  command=input ('>>>')
    if command =="exit":
    time.sleep(0.3)
    quit()
 elif command == "disconnect":
      print ("Disconnecting ...")
      time.sleep(0.3)
      quit()
  else:
       os.system(command)
