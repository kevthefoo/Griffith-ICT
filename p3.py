import time, random

# Quick Sort
def quickSort(arr):
    # If the list has less than 2 elements, it's already sorted
    if len(arr)<=1:
        return arr

    # Choose the middle element as the pivot
    pivot = arr[len(arr) // 2]

    # Partition elements into three groups: less than the pivot, greater than the pivot, and equal to the pivot
    greaterNum = []
    for num in arr:
        if num > pivot:
            greaterNum.append(num)

    lessNum = []
    for num in arr:
        if num < pivot:
            lessNum.append(num)

    equalNum = []
    for num in arr:
        if num == pivot:
            equalNum.append(num)
    
    # Recursively sort the less and greater lists and combine with the equal list
    return quickSort(lessNum) + equalNum + quickSort(greaterNum)

# Merge Sort
def mergeSort(arr):
    # If the list has less than 2 elements, it's already sorted
    if len(arr)<=1:
        return arr
    
    # Find the middle index to divide the array into two halves (left and right)
    midNumIndex = len(arr)//2
    arrLeft = arr[0:midNumIndex]
    arrRight = arr[midNumIndex:]

    # Recursively sort both halves
    leftSort = mergeSort(arrLeft)
    rightSort = mergeSort(arrRight)

    # Merge the sorted left and right halves into a single sorted list
    mergedArr = []
    i = 0
    j = 0

    # Compare elements from both halves and append the smaller one to mergedArr
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

# Insertion Sort
def insertSort(arr):
    # Initialize the sorted array with the first element
    target = arr[0]
    sortedArr = []
    sortedArr.append(target)
    
    # Loop through the remaining elements of the input array
    for i in range(1, len(arr)):
        compareNum = arr[i]

        # If the current number is smaller than the first element in sortedArr, insert it at the beginning
        if compareNum < sortedArr[0]:
            sortedArr.insert(0, compareNum)
            continue
        
        inserted = False

        # Find the correct position in sortedArr for insertion
        for _ in sortedArr:
            if compareNum < _:
                sortedArr.insert(sortedArr.index(_), compareNum)
                inserted = True
                break
        
        # If the number is larger than all elements in sortedArr, append it to the end
        if not inserted:
            sortedArr.append(compareNum)

    return sortedArr

# Selection Sort
def selectionSort (arr):
    # Create an empty list to store the sorted elements
    sortedArr = []
    
    while len(arr) > 0:
        # Assume the first element is the minimum
        minNum = arr[0]

        # Find the real minimum number in the array
        for num in arr:
            if num < minNum:
                minNum = num

        # Append the minimum number to the sorted array
        sortedArr.append(minNum)

        # Remove the minimum number from the originla array
        arr.remove(minNum)

    
    return sortedArr



# Performance Testing
sizes = [1000, 5000, 10000, 20000, 30000, 40000, 50000, 100000]

# -------------------------------- Random Array Test--------------------------------
# Generate a random array
for size in sizes:
    randomArray = []
    for n in range(size):
        randomArray.append(n)

    # Shuffle the array
    random.shuffle(randomArray)

    with open("random_array.txt", "a") as f:
        f.write(f"Size of the array: {size}\n")
    


    startTime = time.time()
    result = quickSort(randomArray)
    endTime = time.time()
    with open("random_array.txt", "a") as f:
        f.write(f"Time taken: {endTime - startTime} seconds with QuickSort with {size} elements in an random array\n")
    print(f"Time taken: {endTime - startTime} seconds with QuickSort with {size} elements in an random array")

    startTime = time.time()
    mergeSort(randomArray)
    endTime = time.time()
    with open("random_array.txt", "a") as f:
        f.write(f"Time taken: {endTime - startTime} seconds with MergeSort with {size} elements in an random array\n")
    print(f"Time taken: {endTime - startTime} seconds with MergeSort with {size} elements in an random array")

    startTime = time.time()
    insertSort(randomArray)
    endTime = time.time()
    with open("random_array.txt", "a") as f:
        f.write(f"Time taken: {endTime - startTime} seconds with InsertSort with {size} elements in an random array\n")
    print(f"Time taken: {endTime - startTime} seconds with InsertSort with {size} elements in an random array")

    startTime = time.time()
    selectionSort(randomArray)
    endTime = time.time()
    with open("random_array.txt", "a") as f:
        f.write(f"Time taken: {endTime - startTime} seconds with selectionSort with {size} elements in an random array\n\n")
    print(f"Time taken: {endTime - startTime} seconds with selectionSort with {size} elements in an random array")


# -------------------------------- Reversed Array Test--------------------------------
# Generate a reversed sorted array
for size in sizes:
    reverseArray = []
    for n in range(size):
        reverseArray.append(n)

    reverseArray.reverse()

    with open("reversed_array.txt", "a") as f:
        f.write(f"Size of the array: {size}\n")
    
    startTime = time.time()
    result = quickSort(reverseArray)
    endTime = time.time()
    with open("reversed_array.txt", "a") as f:
        f.write(f"Time taken: {endTime - startTime} seconds with QuickSort with {size} elements in an reversed array\n")
    print(f"Time taken: {endTime - startTime} seconds with QuickSort with {size} elements in an reversed array")

    startTime = time.time()
    mergeSort(reverseArray)
    endTime = time.time()
    with open("reversed_array.txt", "a") as f:
        f.write(f"Time taken: {endTime - startTime} seconds with MergeSort with {size} elements in an reversed array\n")
    print(f"Time taken: {endTime - startTime} seconds with MergeSort with {size} elements in an reversed array")

    startTime = time.time()
    insertSort(reverseArray)
    endTime = time.time()
    with open("reversed_array.txt", "a") as f:
        f.write(f"Time taken: {endTime - startTime} seconds with InsertSort with {size} elements in an reversed array\n")
    print(f"Time taken: {endTime - startTime} seconds with InsertSort with {size} elements in an reversed array")

    startTime = time.time()
    selectionSort(reverseArray)
    endTime = time.time()
    with open("reversed_array.txt", "a") as f:
        f.write(f"Time taken: {endTime - startTime} seconds with selectionSort with {size} elements in an reversed array\n\n")
    print(f"Time taken: {endTime - startTime} seconds with selectionSort with {size} elements in an reversedom array")

# -------------------------------- Duplicate Value Array Test--------------------------------
# Generate a duplicate value array
for size in sizes:
    duplicateArray = []
    for n in range(size):
        duplicateArray.append(random.randint(0, 10))


    with open("duplicate_array.txt", "a") as f:
        f.write(f"Size of the array: {size}\n")
    

    startTime = time.time()
    result = quickSort(duplicateArray)
    endTime = time.time()
    with open("duplicate_array.txt", "a") as f:
        f.write(f"Time taken: {endTime - startTime} seconds with QuickSort with {size} elements in an duplicate value array\n")
    print(f"Time taken: {endTime - startTime} seconds with QuickSort with {size} elements in an duplicate value array")

    startTime = time.time()
    mergeSort(duplicateArray)
    endTime = time.time()
    with open("duplicate_array.txt", "a") as f:
        f.write(f"Time taken: {endTime - startTime} seconds with MergeSort with {size} elements in an duplicate value array\n")
    print(f"Time taken: {endTime - startTime} seconds with MergeSort with {size} elements in an duplicate value array")

    startTime = time.time()
    insertSort(duplicateArray)
    endTime = time.time()
    with open("duplicate_array.txt", "a") as f:
        f.write(f"Time taken: {endTime - startTime} seconds with InsertSort with {size} elements in an duplicate value array\n")
    print(f"Time taken: {endTime - startTime} seconds with InsertSort with {size} elements in an duplicate value array")

    startTime = time.time()
    selectionSort(duplicateArray)
    endTime = time.time()
    with open("duplicate_array.txt", "a") as f:
        f.write(f"Time taken: {endTime - startTime} seconds with selectionSort with {size} elements in an duplicate value array\n\n")
    print(f"Time taken: {endTime - startTime} seconds with selectionSort with {size} elements in an duplicate value array")



# -------------------------------- Extreme Value Array Test--------------------------------
# Generate a extreme value array
# for size in sizes:
#     extremeArray = []
#     for n in range(size):
#         extremeArray.append(n)


#     with open("extreme_array.txt", "a") as f:
#         f.write(f"Size of the array: {size}\n")
    


#     startTime = time.time()
#     result = quickSort(extremeArray)
#     endTime = time.time()
#     with open("extreme_array.txt", "a") as f:
#         f.write(f"Time taken: {endTime - startTime} seconds with QuickSort with {size} elements in an extreme value array\n")
#     print(f"Time taken: {endTime - startTime} seconds with QuickSort with {size} elements in an extreme value array")

#     startTime = time.time()
#     mergeSort(extremeArray)
#     endTime = time.time()
#     with open("extreme_array.txt", "a") as f:
#         f.write(f"Time taken: {endTime - startTime} seconds with MergeSort with {size} elements in an extreme value array\n")
#     print(f"Time taken: {endTime - startTime} seconds with MergeSort with {size} elements in an extreme value array")

#     startTime = time.time()
#     insertSort(extremeArray)
#     endTime = time.time()
#     with open("extreme_array.txt", "a") as f:
#         f.write(f"Time taken: {endTime - startTime} seconds with InsertSort with {size} elements in an extreme value array\n")
#     print(f"Time taken: {endTime - startTime} seconds with InsertSort with {size} elements in an extreme value array")

#     startTime = time.time()
#     selectionSort(extremeArray)
#     endTime = time.time()
#     with open("extreme_array.txt", "a") as f:
#         f.write(f"Time taken: {endTime - startTime} seconds with selectionSort with {size} elements in an extreme value array\n\n")
#     print(f"Time taken: {endTime - startTime} seconds with selectionSort with {size} elements in an extreme value array")














# The results show that QuickSort and MergeSort are significantly faster than InsertSort and selectionSort for larger arrays.
# QuickSort and MergeSort have a time complexity of O(n log n), while InsertSort and selectionSort have a time complexity of O(n^2).
# This demonstrates the efficiency of divide-and-conquer algorithms like QuickSort and MergeSort for sorting large datasets.
# The time taken for each sorting algorithm increases with the size of the array, but QuickSort and MergeSort remain efficient even for larger datasets.
# The results also highlight the importance of choosing the right sorting algorithm based on the size and nature of the data.
# The performance of sorting algorithms can vary based on the characteristics of the input data, such as whether it is already partially sorted or contains many duplicate elements.
# In practice, QuickSort is often preferred for its average-case performance and in-place sorting capabilities, while MergeSort is used when stable sorting is required or when dealing with linked lists.
# The choice of sorting algorithm can also depend on the specific requirements of the application, such as memory constraints and the need for stability in sorting.
# Overall, the results demonstrate the effectiveness of QuickSort and MergeSort for sorting large arrays, while highlighting the limitations of InsertSort and selectionSort for larger datasets.
