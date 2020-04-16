import pprint

print("Input character:")
character = input()
count = {}

for cha in character:
  count.setdefault(cha,0)
  (count[cha]) += 1

pprint.pprint(count)