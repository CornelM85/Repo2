from classes import Appointment


def todo_list():
    name = Appointment()

    def choose():
        """ This function loops and lets you choose from 4 options available"""
        return input('You have 5 options to choose from:\n'
                     '1 -> New Task\n'
                     '2 -> Finnish Task\n'
                     '3 -> List all Tasks\n'
                     '4 -> Get details for a Task\n'
                     '_____________________\n'
                     'quit -> Exit\n'
                     'Your choice: ')

    def menu():
        """This function ask you if you want to return to your main menu"""
        answer = input('\nReturn to menu? y/n\n')
        while answer != ('y', 'n'):
            if answer.lower() not in ('n', 'y'):
                print('Please enter the correct option!')
                answer = input('\nReturn to menu? y/n\n')

            elif answer.lower() == 'n':
                exit(0)

            else:
                return choose()

    choice = choose()

    while choice != 'quit':

        if choice == '1':
            task_name = input('Please enter the name of the Task:\n')
            name.add_task(task_name)

        elif choice == '2':
            task_finish = input('Please enter the Task name you wish to finnish:\n')
            name.finish_task(task_finish)

        elif choice == '3':
            name.get_tasks()

        elif choice == '4':
            task_name = input('Please enter the task name:\n')
            name.get_task_details(task_name)

        elif choice == 'quit':
            break

        else:
            print('Please provide a valid choice!')

        choice = menu()

