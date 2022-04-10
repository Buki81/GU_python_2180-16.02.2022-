class Road:

    def __init__(self, length, width, wt, depth):
        self._length = length # метры
        self._width = width # метры
        self._wt = wt # килограммов на 1 см тольщины(глубины) асфальта
        self._depth = depth # сантиметров асфальта
        self.asphalt()

    def asphalt(self):
        print(f'{int (self._length * self._width * self._wt * self._depth / 1000)} тонн асфальта')


a = Road(20, 5000, 25, 5)
