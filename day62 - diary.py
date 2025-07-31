#This lesson required the use of the Replit database, which is a paid feature, therefore I did it using a csv file.

import datetime, csv, os, time

pin = "298205"
entries = []

if os.path.exists("diary.csv"):
  with open("diary.csv", mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
      if row:
        entries.append(f"{row[0]} : {row[1]}")

def clear():
  time.sleep(0.5)
  os.system("clear")
  
def unlock():
  guess = input("Enter pin: ")
  if guess == pin:
    return True
  else:
    print("Error.")
    exit()

def add():
  entry = input("Enter entry: ")
  date = datetime.datetime.now()
  entries.append(f"{date} : {entry}")

  with open("diary.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([date, entry])
    
  clear()
  
def view():
  for entry in entries:
    print(f"{entry}\n")
  time.sleep(3)
  os.system("clear")
    

if unlock():
  clear()
  while True:
    action = input("Welcome to the diary.\nWould you like to 1. Add or 2. View: ")
    if action == "1":
      add()
    elif action == "2":
      view()
    else:
      print("Please enter a valid action.")



  
