#! python3
# Section 8 practice on file module

#Mad Libs - replace specfic words in text with other words.

f = open('madlib.txt')
text = f.read()

adj = str(input('Enter an adjective:\n'))
noun1 = str(input('Enter a noun:\n'))
verb = str(input('Enter a verb:\n'))
noun2 = str(input('Enter a noun:\n'))

text = text.replace('ADJECTIVE', adj)
text = text.replace('NOUN', noun1, 1)
text = text.replace('VERB', verb)
text = text.replace('NOUN', noun2, 1)

print(text)
with open('madlib_replace.txt', 'w') as f:
  f.write(text)
f.close()