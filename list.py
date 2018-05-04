import random

def randomList():
    randomlist = random.sample(range(1,100),50)
    randomlist.sort()
    return randomlist 

def meanOfList(randomlist):

    return sum(randomlist) / float(len(randomlist))

def medianOfList(randomlist):
    median = int((len(randomlist)+1) / 2)
    print (median)
    return randomlist[median]

def modeOfList(randomlist):
    for i in range(0,len(randomlist)):
        for y in range(i + 1, len(randomlist)):
            if randomlist[i] == randomlist[y]:
                return True
    return False                  
        



# print(randomList())
# print(medianOfList(randomList()))
print(modeOfList(randomList()))

#print(meanOfList(randomList()))