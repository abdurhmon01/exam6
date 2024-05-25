class Staff:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary
class Techer(Staff):
    def show_info(self):
        return f"{self.role}, {self.department}, {self.salary}"
per=Techer(role="malim",department="programist",salary="6000s")
print(per.show_info())
