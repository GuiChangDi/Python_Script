def collatz(number):
  if number % 2 == 0:
    number = number // 2
    print(number)
  else:
    number = 3*number + 1
    print(number)
  return number

print('Enter number:')
try:
  a = int(input())
  while a != 1: 
    a = collatz(a)
    continue
except ValueError:
  print('Input must be intger')