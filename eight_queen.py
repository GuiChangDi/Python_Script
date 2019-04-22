def conflict(state,nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i): 
            return True
    return False

def queens(num = 8,state = ()):
    for pos in range(num):
        if not conflict(state,pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens(num,state+(pos,)):
                    yield (pos,) + result

def prettyprint(Solution):
    def line(pos,length=len(Solution)):
        return '. ' * (pos) + 'X ' + '. ' *(length-pos-1)
    for pos in Solution:
        print(line(pos))

if __name__ == '__main__':
    import random
    a = int(input('Input the num:'))
    prettyprint(random.choice(list(queens(a))))
    print('Total results count = '+ str(len(list(queens(a)))))
    