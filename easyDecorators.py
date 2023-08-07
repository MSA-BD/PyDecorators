'''
What is decorators in python?
We used Decorators to add additional functionalities to an existing function.
Accepting functions as argument and defining function inside other function.
***Decorators is a callable python object that is take other function as parametre and add some functionalities and
return a function.***
'''
# def outer_fun(n):
#     print(f"Im in outer function {n}")
#     def inner_func(n):
#         print(f"I'm in inner function {n}")
#     inner_func(n)
# outer_fun(1)

# def outer_fun(n):
#     print(f"Im in outer function {n}")
#     def inner_func():
#         return ("I'm in inner function")
#     return inner_func
#
# inner_value=outer_fun(1)
# print(inner_value())

# def decoratorFunc(additionFunc):
#     def innerFunc():
#         additionValue=additionFunc()+float(input("Enter third number: "))
#         return additionValue
#     return innerFunc
# def addition():
#     return  float(input("Enter the first number: "))+float(input("Enter the first number: "))
# innerFunc=decoratorFunc(addition)
# finalValue=innerFunc()
# print(finalValue)


def addValue(x,y):
    return x+y
def calculate(func):
    def increasing():
      prevValue=func(float(input("Enter x value: ")),float(input("Enter Y value: ")))
      return prevValue+float(input("Enter Z value: "))
    return increasing
increasingFunc=calculate(addValue)
totalValue=increasingFunc()
print(totalValue)
# totalValue=calculate(addValue)()
# print(totalValue)


