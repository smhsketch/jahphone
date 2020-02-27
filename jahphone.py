import os
status = input("Status: ")
command = "twurl -d 'status="+status+"' /1.1/statuses/update.json"
os.system(command)
os.system("clear")
