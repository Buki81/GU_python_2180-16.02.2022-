class Stationery():
    title = 'Запуск отрисовки'
    text = title

    def draw(self, text):
        print(text)


class Pen(Stationery):
    def __init__(self):
        text = 'Рисуем ручкой!!!'
        self.draw(text)


class Pencil(Stationery):
    def __init__(self):
        text = 'Рисуем карандашом!!'
        self.draw(text)
class Handle(Stationery):
    def __init__(self):
        text = 'Рисуем маркером!'
        self.draw(text)

first = Stationery().draw(Stationery().title)
pen = Pen()
pencil = Pencil()
handle = Handle()