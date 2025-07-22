import os, time, random

def menu():
  os.system("clear")
  choice = input("Do you want to? 1. Add an idea or 2. Load a random idea or 3. Clear list --> ")
  if choice == "1":
    idea = input("Enter your idea: ")
    f = open("my.ideas", "a+")
    f.write(f"{idea}\n")
    f.close()
    time.sleep(1)
    os.system("clear")
    
  elif choice == "2":
    f = open("my.ideas", "r")
    ideas = f.read().split("\n")
    f.close()
    ideas.remove("")
    if not ideas:
      print("Cannot complete action, list is empty.")
    else:
      print(random.choice(ideas))
    
    time.sleep(2)
    os.system("clear")

  elif choice == "3":
    f = open("my.ideas", "w")
    f.close()
    print("List cleared.")
    time.sleep(1)
    os.system("clear")
    
    
  else:
    print("Please enter valid action.")
    time.sleep(1)
    os.system("clear")
  

while True:
  menu()

