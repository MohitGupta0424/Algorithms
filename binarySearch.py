#Binary Search
inputArray = [2,4,6,10,23,39,60,63,84]      #Sorted Array
findElement = 4
low = 0
hi = len(inputArray)
flag = False
while low<=hi:
    mid = (hi + low)/2
    if inputArray[mid] == findElement:
        flag = True
        break
    elif inputArray[mid] < findElement:
        low = mid + 1
    else:
        hi = mid - 1
if flag == True:
    print "Element Found."
else:
    print "Element Not Found."
