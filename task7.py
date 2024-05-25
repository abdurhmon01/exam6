class Person:
    def __init__(self,name,counry,birthday):
        self.name=name
        self.counry=counry
        self.birthday=birthday
    def Person_age(self):
        return 2024-self.birthday
    def show_info(self):
        return f"{self.name}, {self.counry}, {self.birthday}"
person=Person(name="Dilovar", counry="tajikistan", birthday=2006)
print(person.show_info())
print(person.Person_age())