#Section 5.1 Inventory
stuff = {'rope':1, 'torch': 6, 'gold coin': 42, 'dager': 1, 'arrow': 12}

def displayInventory(dict):
  print("Inventory:")
  TotalNum = 0
  for k, v in dict.items():
    print(str(v) + ' ' + k)
    TotalNum += v
  print('Total count:' + str(TotalNum))

#Section 5.2
def addToInventory(inventory, addedItems):
  for i in addedItems:
    inv.setdefault(i,0)
    inv[i] += 1
  return inv
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
displayInventory(stuff)