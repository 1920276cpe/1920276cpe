class User():
    def __init__(self, firstname, lastname, age, address, birthday):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.address = address
        self.birthday = birthday
        
    def Describe_User(self):
        print(self.firstname+" "+self.lastname)
        print(self.age)
        print(self.address)
        print(self.birthday)
    
    def greet_use(self):
        print("\nHello there " +self.firstname)
        
Cyrus = User('Edsel','Tiamsim','21','manggas padre garcia batangas','february 25 2001')
Cyrus.Describe_User()
Cyrus.greet_use()

    