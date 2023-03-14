class My:
  name = input("Твоє ім'я   ")
  hight = input("Твій зріст   ")
  gmail = input("Твій gmail   ")

try:
  age = input("Твій вік   ")
  age = int(age)
except:
  print("Не схоже на цифру")
  age = input('твій вік   ')
  age = int(age)

if age < 12:
  print("Малолетка, Хи")

