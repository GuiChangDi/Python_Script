#! python3
# Section7.py practice on regex

import re

# Use regex to check whether input is strong string cmd
len_re = re.compile(r'.{8,}') # length at least 8
a_re = re.compile(r'[a-zA-Z]+') # must contain upper or lower chara
num_re = re.compile(r'[0-9]+') # must contain at least 1 number.

def StrongcmdCheck():
  text = str(input('Input token string:'))
  if num_re.search(text) and len_re.search(text) and a_re.search(text) is not None:
    print('string is strong token.')
  else:
    print('string is not strong token.')

# Use regex to implement strip() method
def re_strip(s, t=r'\s'):
  format = r'^%s*|%s*$' % (t,t)
  reg = re.compile(format)
  text = reg.sub('', s)
  return text

StrongcmdCheck()
print(re_strip(' guichangdi ', 'g'))
