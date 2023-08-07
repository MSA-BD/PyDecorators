# Multiple decorators
def decorUppercaseFunc(fullNameFunc):
    def makeUpperCase():
        return fullNameFunc().upper()
    return makeUpperCase
def decorSplitFunc(fullNameFunc):
    def makeList():
        return fullNameFunc().split()
    return makeList
@decorSplitFunc
@decorUppercaseFunc
def getFullName():
    return input("Enter first name: ")+" "+input("Enter last name: ")

#multiple decorators
print(getFullName())

# capiName=decorUppercaseFunc(getFullName)()
# print(capiName)
# splitName=decorSplitFunc(getFullName)()
# print(splitName)

#eksathe duiti decorators
# getName=decorSplitFunc(decorUppercaseFunc(getFullName))
# print(getName())
