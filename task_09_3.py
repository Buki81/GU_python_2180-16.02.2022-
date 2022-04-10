class Worker:
    def __init__(self, name, surname, position, **kwargs_income):
        self.name = name # Имя
        self.surname = surname # Фамилия
        self.position = position # Должность
        self._income = kwargs_income # Оклад и премия
        # _income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, **kwargs):
        super().__init__(name, surname, position, **kwargs)
        get_full_name = ' '.join([name, surname])
        get_total_income = self._income["wage"] + self._income["bonus"]
        print (f'{get_full_name}, должность: {position}, доход: {get_total_income} рублей в месяц.')


men = Position('Иван', 'Иванов', 'бухгалтер', wage = 50000, bonus = 20000)
