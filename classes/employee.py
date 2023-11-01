class Employee:
    __first_name = None
    __last_name = None
    __salary = None

    def __init__(self, first_name, last_name, salary):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__salary = salary

    def description(self):
        print(f'First Name: {self.__first_name}\n'
              f'Last Name: {self.__last_name}\n'
              f'Salary: {self.__salary} $')

    def fullname(self):
        print(f'Full Name: {self.__first_name + self.__last_name}')

    def monthly_salary(self):
        print(f'The monthly salary is: {self.__salary} $')

    def annually_salary(self):
        print(f'The annual salary is: {self.__salary * 12} $')

    def salary_raise(self, percent):
        self.__salary += self.__salary * (percent / 100)

