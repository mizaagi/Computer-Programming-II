from random import randint
secret_number = randint(1, 21)
user_number = int(input("Your number: "))
print("Computer number: " + str(secret_number))
if secret_number == user_number:
  print("You won!")
else:
  print("Better luck next time.")