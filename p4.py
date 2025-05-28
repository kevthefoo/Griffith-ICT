def searchItem(targetWeight, targetInventory, startIndex=0, endIndex=None):
    if endIndex is None:
        endIndex = len(targetInventory) - 1

    print(f"Start Index: {startIndex}, End Index: {endIndex}")
    midItemIndex = (startIndex + endIndex) // 2

    # If search range is invalid (target not found)
    if startIndex > endIndex:
        # Handle edge cases where startIndex or endIndex is out of bounds
        if startIndex >= len(targetInventory):
            closestIndex = len(targetInventory) - 1
        elif endIndex < 0:
            closestIndex = 0
        else:
            # Choose the closest between endIndex and startIndex
            left = endIndex
            right = startIndex
            if abs(targetInventory[left] - targetWeight) <= abs(targetInventory[right] - targetWeight):
                closestIndex = left
            else:
                closestIndex = right
        print(f"Item is not found. The weight of the closest available item is {targetInventory[closestIndex]}\n")
        return closestIndex

    if targetInventory[midItemIndex] == targetWeight:
        print(f"Item is found at index {midItemIndex}.\n")
        return midItemIndex
    elif targetInventory[midItemIndex] < targetWeight:
        return searchItem(targetWeight, targetInventory, midItemIndex + 1, endIndex)
    else:
        return searchItem(targetWeight, targetInventory, startIndex, midItemIndex - 1)

    

inventory = [10, 20, 30, 40, 50, 60, 70, 80, 90, 91.49, 92.5000001, 92.52]
result = searchItem(92, inventory)
print(f"Item is found at index {result}.\n")

# Analysis and Explanation
# The implemented solution uses Binary Search which is more efficient than linear search in this case
# Time Complexity: Base Case: O(1), Worst Case: O(log n)