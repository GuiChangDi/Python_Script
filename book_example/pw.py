#! python3
#pw.py - An insecure password locker program example.

PASSWORDS = {'email': 'F7miniBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

import sys,pyperclip
if len(sys.argv) < 2:
  print('Usage: python pw.py [account] - copy account password')
  sys.exit()

account = sys.argv[1] #get first command line arg

if account in PASSWORDS.keys():
  pyperclip.copy(PASSWORDS[account])
  print('Password for ' + account + ' copied to clipboard.')
else:
  print('There is no account named: ' + account)
