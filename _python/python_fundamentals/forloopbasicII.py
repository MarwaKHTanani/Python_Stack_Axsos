# biggie size
def biggieSize(arr):
    for i in range(len(arr)):
        if arr[i]>0:
            arr[i]='big'
    return arr
print(biggieSize([-1,3,5,-5]))

count positive
def countPositive(arr):
    count=0
    for i in range(len(arr)):
        if arr[i] >0:
            count+=1
    arr[len(arr)-1]=count
    return arr
# print(countPositive([1,6,-4,-2,-7,-2]))

# sum total
def sumTotal(arr):
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
    return sum
# print(sumTotal([1,2,3,4]))

# average
def average(arr):
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
    return sum/len(arr)
# print(average([1,2,3,4]))

# length
def length(arr):
    return len(arr)
# print(length([1,2]))

# minimum
def minimumNo(arr):
    if arr==[]:
        return False
    min=arr[0]
    for i in range(len(arr)):
        if min > arr[i]:
            min=arr[i]
    return min
# print(minimumNo([37,2,1,-9]))

# maximum
def maximumNo(arr):
    if arr==[]:
        return False
    max=arr[0]
    for i in range(len(arr)):
        if max < arr[i]:
            max=arr[i]
    return max
# print(maximumNo([37,2,1,-9]))

# ultimate analysis
def ultimateAnalysis(arr):
    result={
        'sumTotal':sumTotal(arr),
        'average':average(arr),
        'minimumNo': minimumNo(arr),
        'maximumNo':maximumNo(arr),
        'length':length(arr)
    }
    return result 
# print(ultimateAnalysis([37,2,1,-9]))

# reverse list
def reverse(arr):
    rev_list=[]
    for i in range(len(arr)-1,-1,-1):
        rev_list.append(arr[i])
    return rev_list
# print(reverse([37,2,1,-9]))




