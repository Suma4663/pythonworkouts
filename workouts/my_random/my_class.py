
class Phone:
    #constructor
    def __init__(self,name):
        self.name=name

    def displayname(self):
        return f"This is a report from {self.name}"
class SmartPhone(Phone):
    #constructor
    def __init__(self, device, brand, name):
        super().__init__(name)
        self.device=device
        self.brand=brand

    def description(self):
        return f"{self.device} of {self.brand} supports Android14!"

    def displayname(self):
        return f"This is an advanced {self.name}"

#Creating object of the class
phoneObj = SmartPhone("Smartphone","Samsung","Mobile")
print(phoneObj.displayname())
print(phoneObj.description())
