class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.go()
        self.show_speed()
        self.turn()
        self.stop()

    def go(self):
        print('Вперед!')

    def show_speed(self):
        print(f'Скорость автомобиля {self.speed} км/час.')

    def stop(self):
        print('Stop!')

    def turn(self):
        print('Поворот!')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        print(f'Это {color} городской автомобиль "{name}"')
        if speed > 60:
            print('Превышена скорость движения!')
        print()
        print('Следующий: спортивный автомобиль')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        print(f'Это {color} спортивный автомобиль "{name}"')
        print()
        print('Следующий: рабочий автомобиль')


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        print(f'Это {color} городской автомобиль "{name}"')
        if speed > 40:
            print('Превышена скорость движения!')
        print()
        print('Следующий: полицейский автомобиль')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=None):
        super().__init__(speed, color, name, is_police)
        if is_police:
            print(f'Это {color} полицейский автомобиль "{name}"')
        else:
            print(f'Это {color} РЯЖЕННЫЙ автомобиль "{name}"')


town = TownCar(70, 'черный', 'Запорожец')
sport = SportCar(110, 'красный', 'BMW')
work = WorkCar(35, 'серый', 'GAZ')
polce = PoliceCar(90, 'черный', 'Волга', True)
