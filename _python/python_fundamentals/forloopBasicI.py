# 0-150
for x in range(0,150):
    print(x)

# multiples of 5 from 5 to 1,000
for x in range(5,1000,5):
    print(x)

# counting the dojo way
for x in range(1,100):
    if(x%5==0):
        print('Coding')
    elif(x%10==0):
        print('Coding Dojo')

# whoa that sucker's huge
sum=0
for x in range(0,500000):
    if(not x%2==0):
        sum+=x 
print(sum)

# countdown by fours
for x in range(2018,0,-4):
    print(x)

# flexible counter
lowNum=2
highNum=9
mult=3
for x in range(lowNum,highNum+1):
    if(x%mult==0):
        print(x)
