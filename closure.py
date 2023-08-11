def makeCounter():
    count=0
    def increamentCounter():
        nonlocal count
        count+=1
        return count
    return increamentCounter
innerFunc=makeCounter()
print(innerFunc()) #1
print(innerFunc()) #2