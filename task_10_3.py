class Cell:
	def __init__(self, unit):
		self.unit = unit

	def make_order(self, row):
		if self.unit % row == 0:
			return f"{(('*' * row) + '/n') * (self.unit // row - 1)}{'*' * row}"
		else:
			return f"{(('*'* row)+'/n') * (self.unit // row)}{'*'* (self.unit % row)}"

	def __add__(self, other):
		return f'Сумма ячеек 2-х клеток: {self.unit + other.unit}'

	def __sub__(self, other):
		if self.unit < other.unit:
			raise ValueError('Ячеек в первой клетке меньше, чем во второй.')
		return f'Разница ячеек 2-х клеток: {self.unit - other.unit}'

	def __mul__(self, other):
		return f'Произведение ячеек 2-х клеток: {self.unit * other.unit}'

	def __floordiv__(self, other):
		return f'Целочисленное деление ячеек 2-х клеток: {self.unit // other.unit}'


unit_1 = 30 # количество ячеек в клетке
unit_2 = 15
row = 5 # количество ячеек в ряду
one = Cell(unit_1)
two = Cell(unit_2)
print(one + two)
print(one - two)
print(one * two)
print(one // two)
print(one.make_order(row))
