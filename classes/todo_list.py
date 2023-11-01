from abc import abstractmethod, ABC
import json
import os


class ToDoList(ABC):

    @abstractmethod
    def add_task(self, name):
        raise NotImplementedError

    @abstractmethod
    def finish_task(self, name):
        raise NotImplementedError

    @abstractmethod
    def get_tasks(self):
        raise NotImplementedError

    @abstractmethod
    def get_task_details(self, name):
        raise NotImplementedError


class Appointment(ToDoList):
    __file = 'todo_list.json'
    __todo = None
    __day = None
    __month = None
    __year = None
    __hour = None
    __minutes = None
    __meeting_date = None
    __description = None

    def add_task(self, name):
        """This method creates and modifies the json file in which we save data"""
        self.__is_file()

        with open(self.__file, 'r+') as file:
            self.__todo = json.load(file)

            if name in self.__todo.keys():
                print(f'The task {name} is already present in the list!')

            else:
                answer = input('Do you want to add this task in the list? yes/no \n')
                if answer.lower() == 'no':
                    print('Ok! Good Bye!')

                elif answer.lower() == 'yes':
                    if name != '':
                        self.__description = input(f'Please add the content of the task name: {name}\n')
                        self.__add_date()

                        if 'None' in self.__meeting_date:
                            print('Please provide a correct data!')

                        else:
                            self.__todo[name] = (self.__description, self.__meeting_date)
                            file.seek(0)
                            file.truncate()
                            json.dump(self.__todo, file, indent=2)

                    else:
                        print('You need to provide a name for the task you want to create!')

                else:
                    print('Please enter the correct answer!')

    def __add_date(self):
        """This is an internal method that helps us input date and time"""
        print('Please provide a date for your meeting: (dd/mm/yyyy: HH:MM)\n')
        try:
            day = input('Day: ')
            if day != '' and int(day) in range(0, 32):
                self.__day = day

            month = input('Month: ')
            if month != '' and int(month) in range(0, 13):
                self.__month = month

            year = input('Year: ')
            if year != '' and int(year) in range(2023, 3000):
                self.__year = year

            hour = input('Hour: ')
            if hour != '' and int(hour) in range(0, 25):
                self.__hour = hour

            minutes = input('Minutes: ')
            if minutes != '' and int(minutes) in range(0, 60):
                self.__minutes = minutes

        except ValueError:
            print('Wrong data insertion!')

        finally:
            self.__meeting_date = (f'{self.__day}/{self.__month}/{self.__year} at '
                                   f'{self.__hour}:{self.__minutes}')

    def finish_task(self, name):
        """This method searches and deletes the task saved in our json file"""
        self.__is_file()

        with open(self.__file, 'r+') as file:
            data = json.load(file)

            if name not in data.keys():
                print('The task name you entered is not present in the list!')

            else:
                data.pop(name)
                file.seek(0)
                file.truncate()
                json.dump(data, file, indent=2)
                print('Your task has been removed from the list!')

    def get_tasks(self):
        """This method prints out the task we have stored in our json file"""
        self.__is_file()

        with open(self.__file, 'r') as file:
            print('You have this tasks in progress:\n'
                  '===============================')
            for key in json.load(file):
                print(f'-> {key}', end='\n')

    def get_task_details(self, name):
        """This method prints out the details for the task we choose"""
        self.__is_file()

        with open(self.__file, 'r') as file:
            data = json.load(file)
            try:
                print(f'Details: {data[name][0]}\n'
                      f'Date: {data[name][1]}')

            except KeyError:
                print('The task name you entered is not present in the list!')

    def __is_file(self):
        """This internal function creates a json file if the file is not found"""
        if not os.path.exists(self.__file):
            with open(self.__file, 'x') as file:
                file.write('{}')

