#  1
def a():
    return 5
print(a())
#  output expectation: 5   true

# 2
def a():
    return 5
print(a()+a())
# output expectation: 10  true

# #3
def a():
    return 5
    return 10
print(a())
# output expectation:5  true

# 4
def a():
    return 5
    print(10)
print(a())
# output expectation:5 10  the output is 5

# 5
def a():
    print(5)
x = a()
print(x)

# output expectation:5 5 the output is 5 none


# 6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))
# output expectation:8  error

# 7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
# output expectation:25  true

# 8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
# output expectation:100 10  true

# 9
def a(b,c):
    if b < c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
# output expectation: 7  true
print(a(5,3))
# output expectation:14   true
print(a(2,3) + a(5,3))
# # output expectation:21  true

# 10
def a(b,c):
    return b+c
    return 10
print(a(3,5))
# output expectation:8  true

# # 11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
# output expectation:500 500 300 500  true

# 12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
# output expectation:500 500 300 300 500  the output is:500 500 300 500

# 13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b = a()
print(b)
# output expectation:500 500 300 300  true

# 14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
# output expectation:1 3 2  true

# 15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
# output expectation:1 3 5 10  true
