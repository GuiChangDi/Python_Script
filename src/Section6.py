tableData = [['apples', 'orange', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
def printTable(list):
  Widths = [0]*len(list)
  for i in range(len(list)):
    Widths[i] = len(list[i][0])
    for j in range(len(list[i])):
      if len(list[i][j]) > Widths[i]:
        Widths[i] = len(list[i][j])
  
  for i in range(len(list)):
    for j in range(len(list[i])):
      print(list[j][i].rjust(Widths[i]),end=' ')
    print('\n')

printTable(tableData)