#Section 4.1
def Lamda(list):
    list[len(list)-1] = 'and '+str(list[len(list)-1])
    return ','.join(list)
#Section 4.2
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
def Lamda1(list):
    for i in range(len(list[0])):
        for j in range(len(list)):
            print(list[j][i], end='')
        print('')