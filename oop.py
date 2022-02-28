# Python Object-Oriented Programming

import datetime


class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first.lower()}.{last.lower()}@company.com"
        Employee.num_of_emps += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee("Musleh", "Khan", 400000)
emp_2 = Employee("Test", "User", 500000)


# print(Employee.__dict__)
# print(emp_1.__dict__)
# print(Employee.num_of_emps)

# Example
emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_2 = "Jane-Doe-50000"

new_str_1 = Employee.from_string(emp_str_1)

print(new_str_1.fullname())

print(Employee.is_workday(datetime.date(2022, 2, 11)))
