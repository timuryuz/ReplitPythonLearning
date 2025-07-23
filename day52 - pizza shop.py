import time, os 

orders = []

try:
  f = open("pizzas.txt", "r")
  pizza = eval(f.read())
  f.close()
except:
  print("Error: No existing order list. A blank list will be created.\n")
  time.sleep(1.5)
  os.system("clear")
  
def newOrder():
  name = input("Please enter the name for your order: ")
  try: 
    quantity = int(input("Enter quantity of pizzas: "))
  except:
    quantity = int(input("Please enter a numeric value: "))

  print("Size codes: S - 1, M - 2, L - 3, XL - 4")
  try:
    size = int(input("Enter the code for the size of your pizza: "))
  except: 
    size = int(input("Please only enter one of the code values: "))

  cost = quantity * size
  print(f"\nYour order will be {cost} dollars.")
  order = [name, quantity, size, cost]
  orders.append(order)
  
  
  time.sleep(2)
  os.system("clear")

def viewOrders():
  print(f"""{"Name":^10}{"Quantity":^10}{"Size":^10}{"Cost":^10}""")
  for row in orders:
    print(f"{row[0]:^10}{row[1]:^10}{row[2]:^10}{row[3]:^10}")
  

while True:
  print("Welcome to my pizza shop!")
  choice = input("Enter action: 1) Start new order 2) View orders: ")
  if choice == "1":
    newOrder()
  elif choice == "2":
    viewOrders()
  else:
    print("Please choose a valid action.")

  f = open("pizzas.txt", "w")
  f.write(str(orders))
  f.close()
  time.sleep(1)
  os.system("clear")
