def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

def lookup(data,label,name):
    return data[label].get(name)

def store(data,full_name):
    names = full_name.split()
    if len(names) == 2 :
        names.insert(1,"")
    labels = 'first','middle','last'

    for label,name in zip(labels,names):
        people = lookup(data,label,name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]

def print_params(x,y,z = 3, *pospar,**keypar):
    print(x,y,z)
    print(pospar)
    print(keypar)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

def binarySearch(data,num,left = 0,right = None):
    if right is None: right = len(data) - 1
    if left >= right:
        assert num == data[right]
        return right
    else:
        middle = (left + right)//2
        if num > data[middle]:
            binarySearch(data,num,middle+1,right)
        else:
            binarySearch(data,num,left,middle)

class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('Aaaaah......')
        else:
            print('No,I am not hungry')

class SongBird(Bird):
    def __init__(self):
        super().__init__(self)
        self.sound = 'Squawk'
    def sing(self):
        print(self.sound)