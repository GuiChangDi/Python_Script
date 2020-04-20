#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

# Create phone regex
phoneRegex = re.compile(r'''(
      (\d{3}|\(\d{3}\))?    # area code 区号只能是3个数字或者括号中的3个数字
      (\s|-|\.)?            # separator 电话号码分隔符可以是空格（\s), 短横(-), 句点(.)
      (\d{3})               # first 3 digits 3个数字
      (\s|-|\.)             # separator 分隔符
      (\d{4})               # last 4 digits 4个数字
      (\s*(ext|x|ext.) \s*(\d{2,5}))?       # extension 可选的分机号：任意数目的空格，接着ext,x或ext,再接着2到5位数字
      )''', re.VERBOSE)

# Create email regex
emailRegex = re.compile(r'''(
  [a-zA-Z0-9._%+-]+     # Username 用户名部分是一个或多个字符，包括小写大写字母，数字，句点，下划线，百分号，加号或短横
  @                     # @ symbol
  [a-zA-Z0-9.-]+        # domain name 域名只允许 字母，数字，句点，短横
  (\.[a-zA-Z]{2,4})     # dot-something 顶级域名 like .com
  )''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
  phoneNum = '-'.join([groups[1],groups[3], groups[5]]) # 找出区号-xxx-xxxx
  if groups[8] != '':
    phoneNum += ' x' + groups[8] # 找出分机号
  matches.append(phoneNum)

for groups in emailRegex.findall(text):
  matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
  pyperclip.copy('\n'.join(matches))
  print('Copied to clipoard:')
  print('\n'.join(matches))
else:
  print('No phone numbers or email adrress found.')

