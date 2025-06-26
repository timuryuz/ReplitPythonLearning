import time, os

toDo = []

def viewAll():
  for row in toDo:
    print(row)
  done = input("\nEnter 'd' when done viewing: ")
  if done == "d":
    os.system("clear")
      
def add():
  task = []
  new = input("What is the task?: ")
  doneBy = input("When should it be done?: ")
  priority = input("What is the priority? (High, Medium, or Low): ")
  task.append(new)
  task.append(doneBy)
  task.append(priority)
  toDo.append(task)
  time.sleep(1)
  os.system("clear")
def edit():
  editChoice = input("What is the name of the task you would like to edit?: ")
  option = input("Would you like to edit the name, date, or priority?: ")
  if option.lower().strip() == "name":
    newName = input("Enter new name: ") 
    for row in range(len(toDo)):
        if toDo[row][0] == editChoice:
          toDo[row][0] = newName
  elif option.lower().strip() == "date":
    newDate = input("Enter new date: ")
    for row in range(len(toDo)):
      if toDo[row][0] == editChoice:
        toDo[row][1] = newDate
  elif option.lower().strip() == "priority":
    newPriority = input("Enter updated priority: ")
    for row in range(len(toDo)):
      if toDo[row][0] == editChoice:
        toDo[row][2] = newPriority
  else:
    print("Error. Choice not recognized. Program failure.")
    time.sleep(1)
    os.system("clear")
    exit()
  time.sleep(1)
  os.system("clear")

def remove():
  delete = input("What is the name of the task you would like to remove?: ")
  for row in toDo:
    if delete not in row:
      print("This task does not exist.")
    else:
      toDo.remove(row)
  time.sleep(1)
  os.system("clear")

print("Welcome to toDo list manager!\n")

while True:
  choice = input("Select choice: View, add, edit, or remove: ")
  print()
  if choice.lower().strip() == "view":
    viewAll()
  elif choice.lower().strip() == "add":
    add()
  elif choice.lower().strip() == "edit":
    edit()
  elif choice.lower().strip() == "remove":
    remove()
  else:
    print("Error. Choice not recognized. Program failure.")
    time.sleep(1)
    os.system("clear")
    exit()
