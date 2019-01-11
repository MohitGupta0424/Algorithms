# Insertion Sort
inputArray = [2,4,6,10,23,84,63,60,39,0]
for i in range(1,len(inputArray)):
    for j in range(0,i):
        if inputArray[j]>=inputArray[i]:
            temp = inputArray[i]
            k = i
            while k > j:
                inputArray[k] = inputArray[k-1]
                k = k-1
            inputArray[j] = temp
for i in range(len(inputArray)):
    print (inputArray[i]),
