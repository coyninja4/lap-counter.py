from time import sleep
from datetime import date

today = date.today()
stop = False
addedlap = False
tags = {}

print('When you have finished using the counter type "stop" and a test file will be made with the results')
sleep(1)

while stop == False:
    key = input("waiting: ")
    if key == "stop":
        stop = True
        break
    elif key in tags:
        #gets list stored in dict and stores as data
        data = tags[key]
        data[1] += 1
        print(f"name: {data[0]}, laps: {data[1]}")
    else:
        #assigns tag id in dict with list containing name and starts at lap 0
        tags[key] = list((input("Enter name: "), 0))
f = open(f"laps{today}.txt", 'x')
for i in tags:
    with open(f"{f}", "a") as f:
        f.write(f"{i}")
