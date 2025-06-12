import os, time
print("To-do List Mananger.")

toDo = []

def clear():
  time.sleep(1)
  os.system("clear")
  
def view():
  for i in toDo:
    print(i)
  done = input("Enter 'd' when done viewing: ")
  if done == "d":
    clear()

def check(task):
  if task in toDo:
    return True
  else : 
    return False

def add():
  new = input("Enter task: ")
  if check(new):
    print("This task already exists. Please enter a new task")
  else :
    toDo.append(new)
  clear()
  
def remove():
  unwanted = input("Enter task for deletion: ")
  if check(unwanted):
    toDo.remove(unwanted)
  else:
    print("Task is not in list. Please choose a task that is in the list.")
  clear()
  
def change():
  oldTask = input("Enter task that needs to be changed: ")
  if check(oldTask):
    index = toDo.index(oldTask)
    newTask = input("Enter new task: ")
    toDo[index] = newTask
  else :
    print("Task is not in list. Please choose a task that is in the list.")
  clear()
  
while True :
  choice = input("\nWelcome to your to-do list. Choose action:\n1. View\n2. Add\n3. Remove\n4. Change\n5. Exit\n")
  if choice == "1":
    view()
  elif choice == "2":
    add()
  elif choice == "3":
    doubleCheck = input("Are you sure you want to remove something?(y/n): ")
    if doubleCheck == "y" :
      remove()
    else:
      clear()
      continue
  elif choice == "4": 
    change()
  elif choice == "5":
    os.system("clear")
    exit()


