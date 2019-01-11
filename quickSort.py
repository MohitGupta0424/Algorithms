# Quick Sort

# Partion function to partition along the chosen pivot
def partition(inputArray, low, high):
    pivot = inputArray[high]
    i = low -1
    for j in range(low, high):
        if inputArray[j] <= pivot:
            i = i+1
            temp = inputArray[j]
            inputArray[j] = inputArray[i]
            inputArray[i] = temp
    temp = inputArray[i+1]
    inputArray[i+1] = inputArray[high]
    inputArray[high] = temp
    return i+1

# Recusive quickSort algorithm
def quickSort(inputArray, low, high):
    if low < high:
        pivotPosition = partition(inputArray, low, high)
        quickSort(inputArray, low, pivotPosition-1)
        quickSort(inputArray, pivotPosition+1, high)

# calling Recusive quickSort and printing the output sorted array
inputArray = [2,4,6,10,23,84,63,60,39,0]
quickSort(inputArray,0,len(inputArray)-1)
for i in range(len(inputArray)):
    print (inputArray[i]),
