from random import randint as rd
class Matrix:
	def __init__(self, n):
		self.matr = [[rd(1, n*3) for _ in range(n)] for _ in range(n)]

	def __add__(self, other):
		fin = []
		for i in range(len(self.matr)):
			fin.append([])
			for j in range(len(self.matr[0])):
				fin[i].append(self.matr[i][j] + other.matr[i][j])
		return '\n'.join(map(str, fin))

	def __str__(self):
		return '\n'.join(map(str, self.matr))


n = 5
matr_1, matr_2 = Matrix(n), Matrix(n)
print(matr_1)
print('_____')
print(matr_2)
print('_____')
print(matr_1 + matr_2)
