#!/Library/Frameworks/Python.framework/Versions/3.6/bin/Python3.6
import math
import code


class Number:
	__slots__ = ("num", "ind")

	def __init__(self, num, ind):
		self.num = float(num)
		self.ind = int(ind)
		self.__adjust()

	def __adjust(self):
		add_pow = math.log(abs(self.num), 10)
		add_pow = math.floor(add_pow)
		self.num /= 10 ** add_pow
		self.ind += add_pow

	def __str__(self):
		return "%.3f * 10^%d" % (self.num, self.ind)

	def __add__(self, other):
		return Number(self.num * 10 ** (self.ind - toNumber(other).ind) + toNumber(other).num, toNumber(other).ind)

	def __sub__(self, other):
		return Number(self.num * 10 ** (self.ind - toNumber(other).ind) - toNumber(other).num, other.ind)

	def __mul__(self, other):
		return Number(self.num * toNumber(other).num, self.ind + toNumber(other).ind)

	def __truediv__(self, other):
		return Number(self.num / toNumber(other).num, self.ind - toNumber(other).ind)

	def __pow__(self, other):
		try:
			other_int = int(other)
			return Number(self.num ** other_int, self.ind * other_int)
		except ValueError:
			raise ValueError("power with non-int %s is not supported now" % other)

	def __float__(self):
		return self.num * 10 ** self.ind


class Vector2:
	__slots__ = ("x", "y")

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "%s i + %s j" % (self.x, self.y)

	def __add__(self, other):
		if type(other) == Vector2:
			return Vector2(self.x + other.x, self.y + other.y)
		else:
			raise ValueError("vector + %s operation is undefined" % other)

	def __sub__(self, other):
		if type(other) == Vector2:
			return Vector2(self.x - other.x, self.y - other.y)
		else:
			raise ValueError("vector - %s operation is undefined" % other)

	def __mul__(self, other):
		number = toNumber(other)
		if type(number) == Number:
			return Vector2(self.x * other, self.y * other)
		elif type(number) == Vector2:
			return toNumber(self.x * other.x + self.y * other.y)
		else:
			raise ValueError("vector * %s operation is undefined" % other)

	def __truediv__(self, other):
		return Vector2(self.x / toNumber(other), self.y / toNumber(other))

	def __pow__(self, other):
		return self.magnitude() ** toNumber(other)

	def magnitude(self):
		return (self.x ** 2 + self.y ** 2) ** 0.5

	def unit_vector(self):
		return self / self.magnitude()


# constants
K_const = Number(8.99, 9)
e0_const = Number(8.854, -12)
qe_const = Number(1.602, -19)
Mp_weight = Number(1.673, -27)
Me_weight = Number(9.109, -31)
PI = Number(3.1416, 0)


# object creators
def create_number(description):
	return Number(input("Enter %s's numberic part: " % description), input("Enter %s's index part: " % description))


def create_vector2(description):
	x = input("Enter %s's X part: " % description)
	y = input("Enter %s's Y part: " % description)
	power = input("Enter %s's power: " % description)
	return Vector2(Number(x, power), Number(y, power))


def toNumber(var):
	if type(var) == Number:
		return var
	if type(var) == Vector2:
		return var
	try:
		float(var)
	except ValueError:
		raise ValueError("Cannot cast %s into a number or vector")
	return Number(float(var), 0)


### all avaliable functions

def electric_field():
	q = create_number("charge Q")
	r = create_number("distance r")
	E = K_const * q / r ** 2
	print("answer:", E)
	return E


def electric_potential():
	q = create_number("charge Q")
	r = create_number("distance r")
	V = K_const * q / r
	print("answer:", V)
	return V


def electric_potential_energy():
	q1 = create_number("charge Q1")
	q2 = create_number("charge Q2")
	r = create_number("distance r")
	U = K_const * q1 * q2 / r
	print("answer:", U)
	return U


### test block
def test():
	pass


print(locals)
test()
code.interact(local=locals())
