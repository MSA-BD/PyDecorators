'''
What is closure: A closure is a function-object and a closure is a
reffernce to the enclosing scope.
A closure is a function object that remembers values from it's
enclosing scope even after the enclosing scope has been destroyed.
'''
# def makeCounter():
#     count=0
#     def increamentCounter():
#         nonlocal count
#         count+=1
#         return count
#     return increamentCounter
# innerFunc=makeCounter()
# print(innerFunc()) #1
# print(innerFunc()) #2

def makeCounter2(inValue):
    def increamentCounter2():
        nonlocal count
        count+=inValue
        return count
    count=0
    return increamentCounter2
innerFunc2=makeCounter2(10)
print(innerFunc2()) #10
print(innerFunc2()) #20
