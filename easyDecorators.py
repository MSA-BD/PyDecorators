'''
What is decorators in python?

'''
# def outer_fun(n):
#     print(f"Im in outer function {n}")
#     def inner_func(n):
#         print(f"I'm in inner function {n}")
#     inner_func(n)
# outer_fun(1)

def outer_fun(n):
    print(f"Im in outer function {n}")
    def inner_func():
        return ("I'm in inner function")
    return inner_func

inner_value=outer_fun(1)
print(inner_value)