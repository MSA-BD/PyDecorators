# Multiple decorators
def decorUppercaseFunc(fullNameFunc):
    def makeUpperCase():
        return fullNameFunc().upper()
    return makeUpperCase
def decorSplitFunc(fullNameFunc):
    def makeList():
        return fullNameFunc().upper().split()
    return makeList
def getFullName():
    return input("Enter first name: ")+" "+input("Enter last name: ")

# capiName=decorUppercaseFunc(getFullName)()
# print(capiName)
# splitName=decorSplitFunc(getFullName)()
# print(splitName)
