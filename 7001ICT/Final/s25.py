## Modules and classess
# __init__
# __str__
# superclass and subclass

class GoCard:
    def __init__(self):
        self.balance = 0
        self.ride = 0

    def __str__(self):
        return f"Balance: {self.balance}\nRide: {self.ride}"
    
    def topUp(self, amount):
        self.balance  = self.balance + amount

    def finishRide(self, cost):
        self.balance = self.balance-cost
        self.ride += 1

class regularCard(GoCard):
    def __init__(self):
        super().__init__()
        self.discountCount = 0
        self.discount = 0.5

    def finishRide(self, cost):
        if self.discountCount == 0:
            self.balance = self.balance - cost
            self.ride += 1
            if self.ride % 10 == 0:
                self.discountCount = 5
        else:
            self.balance = self.balance - cost*self.discount
            self.discountCount -= 1

        print(f"Ride: {self.ride}")
        print(f"Discount Count: {self.discountCount}")
        print(f"Balance: {self.balance}", end='\n\n')


class pensionerCard(GoCard):
    def __init__(self):
        super().__init__()
        self.discount = 0.5

    def finishRide(self, cost):
        self.balance = self.balance - cost*self.discount
        self.ride += 1
        print(f"Ride: {self.ride}")
        print(f"Balance: {self.balance}", end='\n\n')

kevin = pensionerCard()
kevin.topUp(20)

paul = regularCard()
paul.topUp(20)


# for n in range(20):
#     kevin.finishRide(1)

# for n in range(20):
#     paul.finishRide(1)

print(kevin.__str__())