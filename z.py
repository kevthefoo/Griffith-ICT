# Pronlem 1:

# You are given a positive integer, and your task is to find the sum of its digits using recursion. 
# For example, the sum of the digits of 123 is 1 + 2 + 3 = 6. The function should keep 
# summing the digits until the number becomes 0. 

# Tasks: 
# 1. Write a recursive function sum_of_digits(n) that takes a positive integer n as input and returns the sum of its digits. 
# 2. If n is a single-digit number, return the number itself. 

# Example Input/Output: 
# ● Input: 123 
# ● Output: 6 (1 + 2 + 3 = 6) 
# ● Input: 98765 
# ● Output: 35 (9 + 8 + 7 + 6 + 5 = 35) 
# ● Input: 5 
# ● Output: 5 (Single-digit number)

# def sum_of_digits(n):
#     if n<10:
#         return n
    
#     str_num = str(n)
#     first_digit = int(str_num[0])
#     rest_digit = int(str_num[1:])

#     return first_digit + sum_of_digits(rest_digit)

# ------------------------------------------------------------------------------------------------------------------
# Pronlem 2:

# A restaurant manages incoming online food delivery orders. The system needs to handle 
# orders in a first-come, first-served manner while allowing customers to cancel orders 
# before they are processed. Suppose that there are no priority levels, no need for 
# reordering, and no fixed number of order slots.

# Tasks: 
# 1. Implement the queue using an array. 
# The queue should support: 
# ●  Add order: Enqueue a new order. 
# ●  Process order: Dequeue and remove the order from the queue. 
# ●  View next order: Peek at the next order without removing it. 
# ●  Cancel order: Remove a specific order from the queue. 
# ●  Check if empty: Determine if there are pending orders. 

# 2. Discuss the limitations of using an array-based queue for this implementation. What 
# alternative data structures can improve efficiency when handling cancellations?

# class orderManager():
#     def __init__(self):
#         self.order = []

#     def addOrder(self, order):
#         self.order.append(order)
#         print("Order is added!\n")
    
#     def processOrder(self):
#         print(f"{ self.order[0]} is ready to process!\n")
#         self.order.pop(0)

#     def removeOrder(self, order_to_remove):
#         for order in self.order:
#             if order == order_to_remove:
#                 self.order.remove(order_to_remove)
#                 print("The order is cancelled!\n")
#                 break

#     def nextOrder(self):
#         if len(self.order)>0:
#             print(f"Next order is {self.order[0]}")
#             return self.order[0]
#         else:
#             print("There's no order left.\n")

#     def checkOrder(self):
#         if len(self.order)>0:
#             print(f"There are {len(self.order)} orders in the line!\n")
#         else:
#             print("There are no pending order!\n")
    

# ------------------------------------------------------------------------------------------------------------------

# Pronlem 3:

# This section focuses on implementing and analyzing various sorting algorithms to determine 
# their efficiency across different scenarios. You will benchmark their performance on different 
# input sizes and types of lists, visualize the results, and explore hybrid sorting techniques. 

# Tasks: 
# 1. Benchmark Sorting Algorithms: 
# ○ Implement the following sorting algorithms: 
# ■ QuickSort 
# ■ MergeSort 
# ■ InsertionSort 
# ■ SelectionSort 
# ○ Test their performance on lists of various sizes: 
# ■ 1000, 5000, 10000, 20000, 30000, 40000, 50000, and 100000 
# elements. 
# ○ Run tests on different types of input data: 
# ■ Random lists 
# ■ Reverse sorted lists 
# ■ Lists with extreme value distributions (e.g., mostly small values 
# with a few large outliers) 
# ■ Lists with many duplicate values 
# ○ Visualize execution time results using line graphs. 

# 2. Scenario-Based Analysis: 
# ○ Based on the benchmarks, identify which sorting algorithm performs best 
# under different conditions. 
# ○ Provide an explanation of why certain algorithms perform better in some 
# cases. 
# ○ In what scenario does QuickSort perform poorly? Analyze cases where 
# QuickSort has high time complexity and explain why it happens.

