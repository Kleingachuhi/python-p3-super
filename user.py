#  calliing classes with : 
#         class User(Person):
# --> in the above line of code , the class is the child while the one in brackets happens to be the parent.This is what we call inheritance.



class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False
    def log_in(self):
        self.is_logged_in = True
        print(f"Current logged in status is {self.is_logged_in}")
my_user = User("Klein")
my_user.log_in()