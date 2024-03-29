class LoginManagementSystem:
    storage = {}

    def register(self):
        name = input("Enter your name: ")
        if not name.strip():
            print("Forgot to enter name")
            return

        rollno = input("Enter the roll no: ")
        if not rollno.strip():
            print("Forgot to enter roll no")
            return

        email = input("Enter the email: ")
        if not email.strip():
            print("Forgot to enter email")
            return

        password = input("Enter the password: ")
        if not password.strip():
            print("Forgot to enter password")
            return

        if rollno in self.storage:
            print("User already exists")
        else:
            user_info = [name, rollno, email, password]
            self.storage[rollno] = user_info
            print("Successfully created")

    def login(self):
        rollno = input("Enter your roll no: ")
        if rollno not in self.storage:
            print("User does not exist")
            return

        password = input("Enter your password: ")
        if password != self.storage[rollno]['password']:
            print("Incorrect password")
        else:
            print("Login successful")

    def satus():
        print("1. login
# Usage example
obj = LoginManagementSystem()
obj.register()
obj.login()
print(obj.storage)












class LoginPage:
    users=dict()
    status=0
    roll=""
    def register(self):
        name=input("enter name ")
        rollNo=input("enter id ")
        mail=input("enter mail ")
        password=input("enter password ")

        if rollNo in self.users:
            print("user already exists")
        else:
            self.users[rollNo]=[password,name,mail]
            print("user created successfully")
        print("\n")

    def login(self):
        rollNo=input("enter id ")
        password=input("enter password ")
        if rollNo not in self.users:
            print("user dosn't exists")
        elif(self.users.get(rollNo)[0]!=password):
            print("invalid password")
        else:
            print("successfully login")
            self.status=1
            self.roll=rollNo
        print("\n")

    def checkDetails(self):
        if(self.status==1):
            print("roll no : ",self.roll)
            print("name : ",self.users.get(self.roll)[1])
            print("mail : ",self.users.get(self.roll)[2])
        else:
            print("Login to check details")
            self.login()
            if self.roll not in self.users:
                print("user dosn't exists")
            else:
                self.checkDetails()

    def logout(self):
        if self.status==0:
            print("login to logout")
        else:
            self.roll=0
            print("successfully logged out")


obj=LoginPage()
c=True
while c:
    print("1 register")
    print("2 login")
    print("3 get details")
    print("4 logout")
    choice=int(input("what will you do "))
    print("\n")
    if choice==1:
        obj.register()
    elif choice==2:
        obj.login()
    elif choice==3:
        obj.checkDetails()
    elif choice==4:
        obj.logout()
        c=False
    else:
        print("enter valid option")
        



        
