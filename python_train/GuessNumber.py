import random

secretnumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

for i in range(1,6):
  print('Take a guess.')
  number = int(input())

  if number > secretnumber:
    print('Your guess is too high.')
  elif number < secretnumber:
    print('Your guess is too low')
  else:
    break
if number == secretnumber:
  print('Good job! You guessed my number in '+ str(i)+' guessess!')
else:
  print('Nope. The number I was thinking of was'+str(secretnumber))