import sqlite3
from employee import Employee

conn = sqlite3.connect(":memory:")  # Good for testing
# conn = sqlite3.connect("employee.db")

c = conn.cursor()

# NOTE create table
c.execute(
    """CREATE TABLE employees (
        first TEXT,
        last TEXT,
        pay INTEGER
    )"""
)


def insert_emp(emp):
    with conn:
        c.execute(
            "INSERT INTO employees VALUES (:first, :last, :pay)",
            {"first": emp.first, "last": emp.last, "pay": emp.pay},
        )


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {"last": lastname})
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute(
            """ UPDATE employees SET pay = :pay WHERE first = :first AND last = :last """,
            {"first": emp.first, "last": emp.last, "pay": pay},
        )


def remove_emp(emp):
    with conn:
        c.execute(
            "DELETE FROM employees WHERE first = :first AND last = :last",
            {"first": emp.first, "last": emp.last},
        )


emp_1 = Employee("John", "Doe", 25000)
emp_2 = Employee("Jane", "Doe", 25000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name("Doe")
print(emps)

update_pay(emp_2, 950000)
remove_emp(emp_1)

emps = get_emps_by_name("Doe")
print(emps)


# c.execute(
#     f"INSERT INTO employees VALUES ('{emp_1.first}', '{emp_1.last}', {emp_1.pay})"
# )

# c.execute(
#     "INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay)
# )
# conn.commit()

# # NOTE insert into database
# c.execute(
#     "INSERT INTO employees VALUES (:first, :last, :pay)",
#     {"first": emp_2.first, "last": emp_2.last, "pay": emp_2.pay},
# )
# conn.commit()

# # NOTE Fetch from database
# c.execute("SELECT * FROM employees WHERE last=?", ("Doe",))
# print(c.fetchall())

# c.execute("SELECT * FROM employees WHERE last=:last", {"last": "Doe"})
# print(c.fetchall())
# conn.commit()

conn.close()
