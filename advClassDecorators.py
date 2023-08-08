class ExtraFunc(object):
    def __init__(self,gotTotalFunc):
        self.function=gotTotalFunc
    def __call__(self,*numsList):
        try:
           if any([isinstance(num,str) for num in numsList]):
               raise TypeError('String are not allowed')
           else:
               return self.function(*numsList)
        except Exception as obj:
            print('error: ',obj)
@ExtraFunc
def gotTotal(*nums):
    total=0
    for num in nums:
        total+=num
    return total
print(gotTotal(2,3,4,5,))
print(gotTotal(2,3,'4',5,))
