class DNS:
    def __init__(self):
        self.database = {}
    
    def update(self, domain_name, ipa):
        self.database[domain_name] = ipa

    def lookup(self, domain_name):
        try:
            ipa = self.database[domain_name]
        except:
            return None
        else:
            return ipa

class advancedDNS(DNS):
    def __init__(self):
        super().__init__()
        self.balcklist = []
    
    def addBalcklist(self, ipa):
        self.balcklist.append(ipa)
        
    def lookup(self, domain_name):
        try:
            ipa = self.database[domain_name]
        except:
            return None
        else:
            if ipa in self.balcklist:
                return None
            else:
                return ipa
        

testDNS = advancedDNS()

while True:
    user_input = input("Please Enter Command: ").lower().strip()
    if user_input == 'q':
        break
    
    if user_input.startswith('u'):
        try:
            domain_name = user_input.split(' ')[1]
            ipa = user_input.split(' ')[2]
        except:
            print("Bad Command")
        else:
            testDNS.update(domain_name ,ipa)
    elif user_input.startswith('l'):
        try:
            domain_name = user_input.split(' ')[1]
        except:
            print("Bad Command")
        else:
            result = testDNS.lookup(domain_name)
            print(result)
    elif user_input.startswith('b'):
        try:
            ipa = user_input.split(' ')[1]
        except:
            print('Bad Command')
        else:
            testDNS.addBalcklist(ipa)
    else:
        print("Bad Command")
    