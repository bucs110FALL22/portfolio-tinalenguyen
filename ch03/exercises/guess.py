import random

randNum = random.randint(1, 11)

i=1
while i < 4:
  guess = int(input("What is your guess?"))
  if guess < randNum:
    print("Too Low")
    i+=1
  elif guess > randNum:
    print("Too High")
    i+=1 
  else:
    print("correct!")
    i=4

  
  