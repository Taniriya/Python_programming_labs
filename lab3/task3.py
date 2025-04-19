from abc import ABC, abstractmethod



class Shape(ABC):
	'''
	Абстрактный базовый класс Shape с методами:
	- area() - вычисляет площадь
	- perimeter() - вычисляет периметр
	'''
	@abstractmethod
	def area(self):
		pass
	def perimeter(self):
		pass

class Rectangle(Shape):
	'''
	Дочерний класс Rectangle с дополнительными атрибутами:
	- height (высота)
	- weight (ширина)
	'''
	def __init__(self, height, width):
		self.height = height
		self.width = width
	def area(self):
		return self.height*self.width
	def perimeter(self):
		return self.height*2+self.width*2
		
class Circle(Shape):
	'''
	Дочерний класс Circle с дополнительным атрибутом:
	- radius (радиус)
	'''
	def __init__(self, radius):
		self.radius = radius
	def area(self):
		return 3.14*self.radius**2
	def perimeter(self):
		return 2*3.14*self.radius

class Triangle(Shape):
	'''
	Дочерний класс Triangle с дополнительными атрибутами:
	- side1 (1-ая сторона)
	- side2 (2-ая сторона)
	- side3 (3-яя сторона)
	'''
	def __init__(self, side1, side2, side3):
		self.side1 = side1
		self.side2 = side2
		self.side3 = side3
	def area(self):
		p = self.side1 + self.side2 + self.side3
		return (p*(p-self.side1)*(p-self.side2)*(p-self.side3))**0.5
	def perimeter(self):
		return self.side1 + self.side2 + self.side3

def print_shape_info(shape):
	print('Площадь:', shape.area())
	print('Периметр:', shape.perimeter())


if __name__ == '__main__':
	rec = Rectangle(2, 4)
	cir = Circle(5)
	tri = Triangle(3, 4, 5)
	print_shape_info(rec)
	print_shape_info(cir)
	print_shape_info(tri)