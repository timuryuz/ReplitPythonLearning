import random, os, time

wordBank = ["Lantern", "Keyboard", "Circuit", "Vocal", "Orbit", "Fork", "Whisper", "Glacier", "Tumble", "Picture"]
picked = []
lives = 5;

word = random.choice(wordBank).lower()

hidden = ["_" for letter in word]

while lives > 0 and "_" in hidden:
  time.sleep(1)
  os.system("clear")
  guess = input("Guess a letter: ").lower()
  
  if guess in picked :
    print("You've already guessed that.")
  else :
    picked.append(guess)
    if guess in word :
      print("Correct!")
      for i in range(len(word)):
        if word[i] == guess :
          hidden[i] = guess
          print(hidden)
    else:
      lives -=1
      print(f"Wrong. You have {lives} lives remaining.")
    
if "_" not in hidden:
  os.system("clear")
  print(f"You have won the game! The word was {word}")
else:
  print(f"You lost. The word was {word.upper()}")
  
