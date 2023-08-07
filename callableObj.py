
'''
zekuno function and kuno object zetathe built-in __call__ magic method take, thake callable obj bole.
Python e callable(obj) method true/false return kore.
x=20 is not callable
def add(x,y):
return x+y  add is callable object
add.__call__(30,40) same like add() func
class and function sob somoy-i callable hoy
class and function chara onno kuno object ke callable korte hole tar moddhye magic method __call__ define korte hobe
'''
class Add:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def addition(self):
        return self.a*self.b*self.c
    def __call__(self):
        return self.a/self.b

total=Add(2,4,6)
print(callable(Add)) #True: class are callable
print(total()) #False: instance are not usually callable if there is no __call__ method

