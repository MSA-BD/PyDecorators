# ekti decorator ke ekadik function er moddhye use kora

def decorator(anyFunc):
    def innerFunc(*values):
        for value in values[0:]:
            if value==0:
                return "Can't divided by zero"
        return anyFunc(*values)
    return innerFunc

@decorator
def dividedByTwo(a,b):
    return a/b

@decorator
def dividedByThree(a,b,c):
    return a/b/c

print(dividedByTwo(0,3))
print(dividedByTwo(4,5))
print(dividedByThree(0,4,6))
print(dividedByThree(7,1,3))
