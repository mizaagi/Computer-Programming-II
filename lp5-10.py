num1 = int(input("Enter a non-negative integer: "))
num2 = int(input("Enter another non-negative integer: "))
temp = 0

while num2 > 0:
  temp = num1 % num2
  num1 = num2
  num2 = temp

print(f"The GCD is {num1}.")