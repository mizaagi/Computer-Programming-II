eggs = int(input("Enter # of eggs: "))
dozens = eggs//12
remainder = eggs%12

price = 0.0

if 0 <= dozens < 4:
  price = 0.50
elif 4 <= dozens < 6:
  price = 0.45
elif 6 <= dozens < 11:
  price = 0.40
elif dozens >= 11:
  price = 0.35
else:
  print("The # of eggs is invalid!")

total = (dozens*price) + ((price/12)*remainder)
print("Your total is $" + str(total) + ".")

