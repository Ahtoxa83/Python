import math

figures = []
areas_list = []

try:
	with open (r'figures.txt', "r", encoding = "utf-8") as f:
		for i in f:
			figures.append(i.strip().split(','))

except FileNotFoundError:
	print (FileNotFoundError.args())


class Circle:

	def __init__(self, radius):
		self.r = radius

	def area(self):
		return math.pi * (self.r ** 2)


class Rect:

	def __init__(self, a, b):
		self.a = a
		self.b = b

	def area(self):
		return self.a * self.b


class Triangle:

	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c

	def area(self):
		half_perimeter = (self.a + self.b + self.c)/2
		S = math.sqrt(half_perimeter*(half_perimeter-self.a)
			*(half_perimeter-self.b)*(half_perimeter-self.c))
		return S

for i in figures:
	
	if i[0] == 'Circle':
		circle = Circle(float(i[1])).area()
		areas_list.append(circle)
	
	elif i[0] == 'Rect':
		rect = Rect(float(i[1]), float(i[2])).area()
		areas_list.append(rect)

	else:
		triangle = Triangle(float(i[1]), float(i[2]), float(i[3])).area()
		areas_list.append(triangle)

total = round(sum(areas_list), 2)

result = "Общая сумма площадей геометрических фигур = {s}".format(s = total)

print (result)