from user import User
class Student(User):
    def __init__(self, name, grade):
        print("Trial to see whether the init has been called")
        super().__init__(name)
        self.grade = grade
    def log_in(self):
        super().log_in()
        self.is_in_class = True
        print(f"The student is {self.is_in_class}ly logged in with a grade of {self.grade}")
my_student = Student("Olien", 96)
my_student.log_in()