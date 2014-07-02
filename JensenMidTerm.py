import math

class Polynomial(object):
	def __init__(self, list_form):
		self.list_form = list_form

	def __add__(self, other):
		new_list_form = []
		short_len = min(len(self.list_form), len(other.list_form))

		for i in xrange(short_len):
			new_list_form.append(self.list_form[i] + other.list_form[i])

		new_list_form.extend(self.list_form[i+1:])
		new_list_form.extend(other.list_form[i+1:])

		return Polynomial(new_list_form)

	def __sub__(self, other):
		new_list_form = []
		short_len = min(len(self.list_form), len(other.list_form))

		for i in xrange(short_len):
			new_list_form.append(self.list_form[i] - other.list_form[i])

		new_list_form.extend(self.list_form[i+1:])
		new_list_form.extend(other.list_form[i+1:])

		return Polynomial(new_list_form)

	def __call__(self, value):
		total = 0

		i = 0
		for coefficient in self.list_form:
			total += coefficient * (value**i)
			i += 1

		return total

	def __mul__(self, other):
		temp_list = []

		for coefficient_1 in self.list_form:
			for coefficient_2 in other.list_form:
				temp_list.append(coefficient_1 * coefficient_2)

		slot = 0
		new_list_form = [0]*len(other.list_form)
		for i in xrange(len(self.list_form)):
			new_list_form.append(0)

			for j in xrange(len(other.list_form)):
				new_list_form[slot+j] += temp_list.pop(0)

			slot += 1

		return Polynomial(new_list_form)

	def __str__(self):
		buff = ""

		i = 0
		for coefficient in self.list_form:
			if coefficient != 0:
				if i == 0:
					buff += "%s + " % (coefficient)
				elif i == 1 and coefficient == 1:
					buff += "x + "
				elif i == 1 and coefficient == -1:
					buff += "-x + "
				elif i == 1:
					buff += "%sx + " % (coefficient)
				elif coefficient == 1:
					buff += "x^%i + " % (i)
				elif coefficient == -1:
					buff += "-x^%i + " % (i)
				elif coefficient != 1 and coefficient != -1:
					buff += "%sx^%i + " % (coefficient, i)
			i += 1


		if buff == "":
			buff = "0"


		return buff.rstrip("+ ")

	def solve(self):
		if not (len(self.list_form) == 3):
			return None

		a = self.list_form[2]
		b = self.list_form[1]
		c = self.list_form[0]

		midBase = (-b) / (2.0 * a)

		dev_step_1 = (b**2) - (4 * a * c)
		if dev_step_1 >= 0:
			dev_step_2 = math.sqrt(dev_step_1)
		else:
			return None
		dev_step_3 = dev_step_2 / (2.0 * a)

		root_1 = midBase - dev_step_3
		root_2 = midBase + dev_step_3

		return [root_1, root_2]

def main():
	list_form_F = [4,0,5,0,0,3]
	list_form_G = [0,0,0,0,0,-2]
	list_form_H = [1,1,1,1,1,1,1]
	list_form_I = [1,0,1,0,1,0,1]
	list_form_1 = [5,2]
	list_form_2 = [1,9,3]

	f = Polynomial(list_form_F)
	g = Polynomial(list_form_G)
	h = Polynomial(list_form_H)
	i = Polynomial(list_form_I)
	p1 = Polynomial(list_form_1)
	p2 = Polynomial(list_form_2)

	print "h - i:", h - i
	print "i - h:", i - h
	print "f + g:", f + g
	print "f + h:", f + h
	print "f + i:", f + i
	print "f + f:", f + f

	print "i(-2):", i(-2)
	print "f(0):", f(0)
	print "f(10):", f(10)
	print "g(4):", g(4)
	print "h(e):", h(math.e)
	print "i(pi):", i(math.pi)

	print "f * g:", f * g
	print "i * f:", i * f
	print "f * f:", f * f
	print "g * g:", g * g
	print "i * g:", i * g
	print "h * g:", h * g

	root_1, root_2 = p2.solve()
	print "%s roots: %s and %s" % (p2, root_1, root_2)

if __name__ == "__main__":
	main()