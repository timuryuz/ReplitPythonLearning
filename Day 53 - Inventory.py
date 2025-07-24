import time, os

inventory = []

try:
  f = open("inventory.txt", "r")
  inventory = eval(f.read())
  f.close()
except:
  print("No file found. Creating blank file.")
  time.sleep(1)
  os.system("clear")
  
def view():
  choice = input("Do you want to view 1. Full inventory or 2. A specific item: ")
  if choice == "1":
    print(f"""{"ITEM":^10}{"QUANTITY":^10}""")
    duplicates = []
    for item in inventory:
      if item not in duplicates:
        occurances = inventory.count(item)
        print(f"{item:^10}{occurances:^10}")
        duplicates.append(item)
  elif choice == "2":
    item = input("Enter the item: ").capitalize()
    if item not in inventory:
      print(f"{item} is not in the inventory.")
    else:
      occurances = inventory.count(item)
      print(f"""{"ITEM":^10}{"QUANTITY":^10}""")
      print(f"{item:^10}{occurances:^10}")
    
def add():
  new = input("Enter item to add to inventory: ").capitalize()
  inventory.append(new)
  print(f"{new} has been added to the inventory.")
  
def remove():
  old = input("Enter item to remove from inventory: ").capitalize()
  if old not in inventory:
    print(f"{old} is not in the inventory.")
  else:
    if inventory.count(old) > 1:
      delete = int(input(f"You have {inventory.count(old)} {old}s. How many do you wish to remove: "))
      count = delete
      if delete > inventory.count(old):
        print(f"There are not that many {old}s. Please enter a valid number.")
      else:
        while delete > 0:
          inventory.remove(old)
          delete -= 1
      print(f"{count} {old}s have been removed.")
    else:
      inventory.remove(old)
      print(f"{old} has been removed from the inventory.")
  
  

while True:
  action = input("INVENTORY\n---------\nSelection Action: 1. View 2. Add. 3. Remove: ")
  if action == "1":
    view()
    time.sleep(2)
    os.system("clear")
  elif action == "2":
    add()
    time.sleep(1)
    os.system("clear")
  elif action == "3":
    remove()
    time.sleep(1)
    os.system("clear")
  else:
    print("Please selection a valid action.")
    time.sleep(1)
    os.system("clear")

  f = open("inventory.txt", "w")
  f.write(str(inventory))
  f.close()
  time.sleep(1)
  os.system("clear")
