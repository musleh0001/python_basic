class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return f"{self.first.lower()}.{self.last.lower()}@email.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname)

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    def __str__(self):
        return f"{self.fullname} - {self.email}"


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        print(f"Employee{'s' if len(self.employees) > 1 else ''} list:")
        for emp in self.employees:
            print(f"\t--> {emp.fullname}")


dev_1 = Developer("Musleh", "Khan", 60000, "Python")
dev_2 = Developer("Test", "User", 50000, "JavaScript")

print(dev_1.__repr__())
print(dev_1)
print(dev_1 + dev_2)
print(len(dev_1))

# print(dev_1.prog_lang)
# print(dev_2.email)

# mgr_1 = Manager("Sue", "Smith", 90000, [dev_1])
# mgr_1.print_emps()

# mgr_1.add_emp(dev_2)
# mgr_1.print_emps()
