class orderManager():
    def __init__(self):
        self.order = []

    # Add order to the queue
    def addOrder(self, order):
        self.order.append(order)
        print("Order is added!\n")
    
    # Process the first order in the queue
    def processOrder(self):
        if self.order:
            print(f"{ self.order[0]} is ready to process!\n")
            self.order.pop(0)
        else:
            print("No order to process!\n")

    # Remove a specific order from the queue
    def removeOrder(self, order_to_remove):
        if order_to_remove in self.order:
            self.order.remove(order_to_remove)
            print("The order is cancelled!\n")
        else:
            print("Order not found!\n")

    # View the next order without removing it
    def nextOrder(self):
        if len(self.order)>0:
            print(f"Next order is {self.order[0]}")
            return self.order[0]
        else:
            print("There's no order left.\n")

    # Check if there are pending orders
    def checkOrder(self):
        if len(self.order)>0:
            print(f"There are {len(self.order)} orders in the line!\n")
        else:
            print("There are no pending order!\n")
    

# Analysis and Explanation
# The pop(0) in processOrder() can be inefficient for large queues because it requires shifting all subsequent elements. It's O(n) in time complexity.
# The remove function in removeOrder() also has O(n) complexity because it needs to search through the list to find the order to remove.
# If we use dictionary with order ID as key, then we can achieve O(1) time complexity for both adding and removing ordedrs.