# Kyle Marlia-Conner
# 10/27/24
# Assignment 1.3

def countdown_bottles(bottle_count):
  for i in range(bottle_count, 0, -1):
      if i > 1:
          print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
          print(f"Take one down and pass it around, {i - 1} bottle{'s' if i - 1 > 1 else ''} of beer on the wall.")
      else:
          print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
          print("Take one down and pass it around, 0 more bottles of beer on the wall.")
  print("Time to buy more bottles of beer.")

# Main Program
try:
  bottles = int(input("Enter the number of bottles: "))
  countdown_bottles(bottles)
except ValueError:
  print("Please enter a valid number.")

