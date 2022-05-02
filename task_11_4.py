class Storage:
    def entrance(self, ent, transfer):
        pass


class OfficeMachines(Storage):
    def __init__(self, producer, model, color, quantity, price):
        self.producer = producer
        self.model = model
        self.color = color
        self.quantity = quantity
        self.price = price

class Printer(OfficeMachines):
    def __init__(self, producer, model, color, quantity, price, print_resolution):
        super().__init__(producer, model, color, quantity, price)
        self.print_resolution = print_resolution

class Scanner(OfficeMachines):
    def __init__(self, producer, model, color, quantity, price, scan_resolution):
        super().__init__(producer, model, color, quantity, price)
        self.scan_resolution = scan_resolution

class Xerox(OfficeMachines):
    def __init__(self, producer, model, color, quantity, price, resolution):
        super().__init__(producer, model, color, quantity, price)
        self.resolution = resolution

# producer - производитель
# model - модель
# color - цвет
# price - цена
# entrance - получение
# transfer - перемещение