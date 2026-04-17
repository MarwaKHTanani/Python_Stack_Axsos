import random
def randInt(min=0,max=100):
    if min>max:
        # updateMin=max
        # max=min
        # min=updateMin
        min,max=max,min

    elif max==min:
        return max
    num=random.random()
    return round(num*(max-min)+min)

print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50,max=500))


