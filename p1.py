# Calculate the sum of digits of a number using recursion
def digitSum(n):
    # Return the number itself if it is a single-digit number
    if n < 10:
        return n
    
    # Convert the number to string to access each digit
    strNum = str(n)

    # Retrive the first digit and convert it to int
    firstDigit = int(strNum[0])
    # Retrive the rest of digits and convert it to int
    restDigit = int(strNum[1:])

    return firstDigit + digitSum(restDigit)

# Test usage
result = digitSum(123)
print(f"The sum of digits of 123 is: {result}")

result = digitSum(98765)
print(f"The sum of digits of 98765 is: {result}")

result = digitSum(5)
print(f"The sum of digits of 5 is: {result}")

# Analysis and Explanation
# The function digitSum takes a positive integer n as input and returns the sum of its digits using recursion.
# Time Complexity: O(n), where n is the number of digits in n. This is because the function makes a recursive call for each digit in n.