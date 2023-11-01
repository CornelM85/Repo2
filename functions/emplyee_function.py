from classes import Employee


def employee():
    name = Employee('George', 'Lupu', 3000)
    name.salary_raise(18)
    name.monthly_salary()