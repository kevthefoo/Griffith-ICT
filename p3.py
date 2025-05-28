import time, random

# QuickSort
def quickSort(arr):
    if len(arr)<=1:
        return arr
    
    # Use the middle element as pivot
    pivot = arr[len(arr) // 2]

    greaterNum = []
    for num in arr[0:-1]:
        if num >= pivot:
            greaterNum.append(num)

    lessNum = []
    for num in arr[0:-1]:
        if num < pivot:
            lessNum.append(num)

    return quickSort(lessNum) + [pivot] + quickSort(greaterNum)

def mergeSort(arr):
    if len(arr)<=1:
        return arr
    
    midNumIndex = len(arr)//2
    arrLeft = arr[0:midNumIndex]
    arrRight = arr[midNumIndex:]

    leftSort = mergeSort(arrLeft)
    rightSort = mergeSort(arrRight)



    # Compare left and right array and merge
    mergedArr = []
    i = 0
    j = 0
    while i < len(leftSort) and j < len(rightSort):
        if leftSort[i] <= rightSort[j]:
            mergedArr.append(leftSort[i])
            i += 1
        else:
            mergedArr.append(rightSort[j])
            j += 1
    
    mergedArr = mergedArr + leftSort[i:]
    mergedArr = mergedArr + rightSort[j:]

    return mergedArr

def insertSort(arr):
    target = arr[0]
    sortedArr = []
    sortedArr.append(target)

    for i in range(1, len(arr)):
        compareNum = arr[i]

        if compareNum < sortedArr[0]:
            sortedArr.insert(0, compareNum)
            continue
        
        inserted = False
        for _ in sortedArr:
            if compareNum < _:
                sortedArr.insert(sortedArr.index(_), compareNum)
                inserted = True
                break

        if not inserted:
            sortedArr.append(compareNum)

    
    return sortedArr

def SelectionSort (arr):
    sortedArr = []
    
    while len(arr) > 0:
        minNum = arr[0]
        for num in arr:
            if num < minNum:
                minNum = num
        sortedArr.append(minNum)
        arr.remove(minNum)

    
    return sortedArr

# Generate a random array of 1000 integers
testArray = []
for n in range(100000):
    testArray.append(n)

# Shuffle the array
random.shuffle(testArray)

startTime = time.time()
quickSort(testArray)
endTime = time.time()

print(f"Time taken: {endTime - startTime} seconds with QuickSort")

startTime = time.time()
mergeSort(testArray)
endTime = time.time()
print(f"Time taken: {endTime - startTime} seconds with MergeSort")

startTime = time.time()
insertSort(testArray)
endTime = time.time()
print(f"Time taken: {endTime - startTime} seconds with InsertSort")

startTime = time.time()
SelectionSort(testArray)
endTime = time.time()
print(f"Time taken: {endTime - startTime} seconds with SelectionSort")

# 1000
# Time taken: 0.003264188766479492 seconds with QuickSort
# Time taken: 0.0022249221801757812 seconds with MergeSort
# Time taken: 0.0013077259063720703 seconds with InsertSort
# Time taken: 0.01538705825805664 seconds with SelectionSort

# 5000
# Time taken: 0.0 seconds with QuickSort
# Time taken: 0.023931503295898438 seconds with MergeSort
# Time taken: 0.20273184776306152 seconds with InsertSort
# Time taken: 0.3132917881011963 seconds with SelectionSort

# 10000
# Time taken: 0.020653486251831055 seconds with QuickSort
# Time taken: 0.0279843807220459 seconds with MergeSort
# Time taken: 0.6679341793060303 seconds with InsertSort
# Time taken: 1.3104441165924072 seconds with SelectionSort

# 20000
# Time taken: 0.04881167411804199 seconds with QuickSort
# Time taken: 0.04585862159729004 seconds with MergeSort
# Time taken: 2.767672061920166 seconds with InsertSort
# Time taken: 5.106107950210571 seconds with SelectionSort

# 30000
# Time taken: 0.05002284049987793 seconds with QuickSort
# Time taken: 0.08237409591674805 seconds with MergeSort
# Time taken: 6.081153631210327 seconds with InsertSort
# Time taken: 11.526447296142578 seconds with SelectionSort

# 40000
# Time taken: 0.10033226013183594 seconds with QuickSort
# Time taken: 0.10285806655883789 seconds with MergeSort
# Time taken: 11.329471111297607 seconds with InsertSort
# Time taken: 23.195240259170532 seconds with SelectionSort

# 50000
# Time taken: 0.10627055168151855 seconds with QuickSort
# Time taken: 0.16108059883117676 seconds with MergeSort
# Time taken: 17.022825956344604 seconds with InsertSort
# Time taken: 36.10710859298706 seconds with SelectionSort

# 100000
# Time taken: 0.2216641902923584 seconds with QuickSort
# Time taken: 0.3230922222137451 seconds with MergeSort
# Time taken: 97.29859185218811 seconds with InsertSort
# Time taken: 230.0204803943634 seconds with SelectionSort

# The results show that QuickSort and MergeSort are significantly faster than InsertSort and SelectionSort for larger arrays.
# QuickSort and MergeSort have a time complexity of O(n log n), while InsertSort and SelectionSort have a time complexity of O(n^2).
# This demonstrates the efficiency of divide-and-conquer algorithms like QuickSort and MergeSort for sorting large datasets.
# The time taken for each sorting algorithm increases with the size of the array, but QuickSort and MergeSort remain efficient even for larger datasets.
# The results also highlight the importance of choosing the right sorting algorithm based on the size and nature of the data.
# The performance of sorting algorithms can vary based on the characteristics of the input data, such as whether it is already partially sorted or contains many duplicate elements.
# In practice, QuickSort is often preferred for its average-case performance and in-place sorting capabilities, while MergeSort is used when stable sorting is required or when dealing with linked lists.
# The choice of sorting algorithm can also depend on the specific requirements of the application, such as memory constraints and the need for stability in sorting.
# Overall, the results demonstrate the effectiveness of QuickSort and MergeSort for sorting large arrays, while highlighting the limitations of InsertSort and SelectionSort for larger datasets.
