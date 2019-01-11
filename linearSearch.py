# Linear Search
inputArray = [2,4,6,10,23,84,63,60,39]
findElement = 4
flag = False
for i in range(len(inputArray)):
    if inputArray[i] == findElement:
        flag = True
if flag == True:
    print "Element Found."
else:
    print "Element Not Found."
