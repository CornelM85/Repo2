from classes import Car


def car():
    model = input('Car model: ')
    top_speed = int(input('Car top speed: '))
    name = Car(model, top_speed)

    def choose():
        return input('You have 5 options to choose from:\n'
                     '1 -> Car description\n'
                     '2 -> Car color change\n'
                     '3 -> Car registration\n'
                     '4 -> Car current speed\n'
                     '5 -> Car speed set\n'
                     '6 -> Car stop\n'
                     '_____________________\n'
                     'quit -> Exit\n'
                     'Your choice: ')

    def menu():
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
            name.description()

        elif choice == '2':
            color = input('New color: ')
            name.paint(color)

        elif choice == '3':
            name.register()

        elif choice == '4':
            name.speed()

        elif choice == '5':
            speed = int(input('Speed: '))
            name.accelerate(speed)

        elif choice == '6':
            name.break_now()

        elif choice == 'quit':
            break

        else:
            print('Please provide a valid choice!')

