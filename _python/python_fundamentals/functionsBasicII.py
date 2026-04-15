# countdown
def countdown(num):
    new_list=[]
    for i in range(num,-1,-1):
        new_list.append(i)
    return new_list

print(countdown(5))

# print and return
def printAndReturn(arr):
    print(arr[0])
    return arr[1]

printAndReturn([1,2])
print(printAndReturn([1,2]))

# first plus length
def firstPlusLen(arr):
    return arr[0]+ len(arr)
print(firstPlusLen([1,2,3,4,5]))

# values greater than second
def greaterThanSec(arr):
    sec=arr[1]
    result=[]
    for i in range(len(arr)):
        if i > sec:
            result.append(i)
    return result
print(greaterThanSec([5,2,3,2,1,4]))

# this length that value
def lenValue(size,value):
    new_arr=[]
    for i in range(0,size):
        new_arr.append(value)
    return new_arr
print(lenValue(6,2))

