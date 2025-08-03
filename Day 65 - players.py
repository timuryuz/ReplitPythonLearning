class character():
  name = None
  health = 80
  magicPoints = 80
  
  def __init__(self, name, health, magicPoints):
    self.name = name
    self.health = health
    self.magicPoints = magicPoints
    
  def printInfo(self):
    print(f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magicPoints}")


class player(character):
  nickname = None
  lives = 3
  
  def __init__(self, nickname):
    self.name = "Player 1"
    self.nickname = nickname
    self.health = 100
    self.magicPoints = 20

  def alive(self):
    if player.health > 0:
      return True
    else:
      return False

  def printInfo(self):
    print(f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magicPoints}\nLives: {self.lives}")

timur = player("Timur")
timur.printInfo()
print(timur.alive())
  
class enemy(character):
  def __init__(self, type, strength):
    self.name = name
    self.health = health
    self.magicPoints = magicPoints
    self.type = type
    self.strength = strength

  def printInfo():
    print(f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magicPoints}\nType: {self.type}\nStrength: {self.strength}")

class orc(enemy):
  speed = None
  
  def __init__(self, speed):
    self.name = "Orc"
    self.type = "Orc"
    self.strength = 100
    self.speed = speed

  def printInfo(self):
    print(f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magicPoints}\nType: {self.type}\nStrength: {self.strength}\nSpeed: {self.speed}")

orca = orc(30)
orca.printInfo()
    
class vampire(enemy):
  isDay = True
  
  def __init__(self, isDay):
    self.name = "Vampire"
    self.type = "Vampire"
    self.strength = 100
    self.isDay = isDay

  def printInfo(self):
    print(f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magicPoints}\nType: {self.type}\nStrength: {self.strength}\nIs Day?: {self.isDay}")

vamp = vampire(False)
vamp.printInfo()
