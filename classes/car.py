class Car:

    __brand = 'BMW'
    __color = 'grey'
    __current_speed = 0
    __available_colors = {'blue', 'red', 'black', 'white', 'green', 'purple'}
    __registered = False

    def __init__(self, model, top_speed):
        self.__model = model
        self.__top_speed = top_speed

    def description(self):
        print(f'Brand: {self.__brand}\n'
              f'Model: {self.__model}\n'
              f'Color: {self.__color}\n'
              f'Top Speed: {self.__top_speed} km/h\n'
              f'Registered: {self.__registered}')

    def register(self):
        if not self.__registered:
            self.__registered = True
            print('Car has been registered!')
        else:
            print('Car already registered!')

    def speed(self):
        print(f'Car current speed is: {self.__current_speed} km/h.')

    def paint(self, color):
        if color.lower() in self.__available_colors:
            self.__color = color.lower()
            print('Car color changed successfully!')

        else:
            print('Color not found!')

    def accelerate(self, speed):
        if speed in range(self.__current_speed, self.__top_speed + 1):
            if speed <= self.__current_speed:
                print('The speed that you entered doesn\'t make the car go faster!')
            else:
                self.__current_speed = speed
                self.speed()

        elif speed > self.__top_speed:
            self.__current_speed = self.__top_speed
            self.speed()

        else:
            print('Incorrect speed value added!')

    def break_now(self):
        if self.__current_speed != 0:
            self.__current_speed = 0
            print('The car has stopped!')

        else:
            print('The car is already stopped!')

