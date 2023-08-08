class Divided(object):
    def __init__(self,multiplyFunc):
        self.multiply=multiplyFunc
    def __call__(self,a,b):
        multiplyResult=self.multiply(a,b)
        return multiplyResult/a/b

@Divided
def multiply(x,y):
    return x*y
print(multiply(2,3)) #1


class Multiply(object):
    def __init__(self,additionFunc):
        self.addition=additionFunc
    def __call__(self,m,n):
        additionResult=self.addition(m,n)
        return additionResult*m*n

@Multiply
def add(a,b):
    return a+b
print(add(3,4))
