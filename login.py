 class User:
    def __init__(self,email_address,password,user_name):
        self.email_address=email_address
        self.password=password
        self.user_name=user_name
user=User(input("Enter your Email:\n"),input("Enter your password:\n"),input("Enter your user name:\n")) 
class Student(User):
     def __init__(self,email_address,password,user_name):
         super().__init__(email_address,password,user_name)
student=Student(input("Enter your Email:\n"),input("Enter your password:\n"),input("Enter your user name:\n")) 
class Admin(User):
     def __init__(self,email_address,password,user_name):
         super().__init__(email_address,password,user_name)
     def print_age(self,age):
         self.age=age
         return f"{self.user_name} is {self.age} years."
         
admin=Admin(input("Enter your Email:\n"),input("Enter your password:\n"),input("Enter your user name:\n")) 
print(admin.print_age(34))