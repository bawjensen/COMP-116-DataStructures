from time import gmtime, strftime
import random

class AddressBook(object):
	def __init__(self):
		self.List = []

	def add_person(self, person):
		self.List.append(person)

	def sample(self):
		print random.choice(self.List)

class Person(object):
	def __init__(self, name, DoB, address, mPhone, wPhone, email):
		self.name = name # Object
		self.DoB = DoB # Object
		self.address = address # Object
		self.mPhone = mPhone # Object
		self.wPhone = wPhone # Object
		self.email = email # Object

	def __str__(self):
		print "_______________________________________"
		print "| %s %s, %s %s. %s" % (self.name.title, self.name.lName, self.name.fName, self.name.mName,self.name.suffix)
		print "| Age: %d (DOB: %s %s, %s)" % (self.DoB.age, self.DoB.month, self.DoB.day, self.DoB.year)
		print "| Phone (Mobile): %s" % (self.mPhone.get_number())
		print "| Phone (Work): %s" % (self.wPhone.get_number())
		print "| Email (Work): %s" % (self.email.address)
		print "| \nHome Address:"

		addressLines = self.address.get_lines()
		if addressLines[1] != "":
			print "| %s\n%s\n%s" % (addressLines[0], addressLines[1], addressLines[2])
		else:
			print "| %s\n%s" % (addressLines[0], addressLines[2])
		print "|_______________________________________"

		return ""


class Name(object):
	def __init__(self, fName, lName, mName="", title="", suffix=""):
		self.fName = fName
		self.mName = mName
		self.lName = lName
		self.title = title
		self.suffix = suffix

class DoB(object):
	def __init__(self, day, month, year):
		self.day = day
		self.month = month
		self.year = year

		#cMonth = strftime('%B', gmtime)
		cYear = strftime('%Y', gmtime())

		self.age = int(cYear) - self.year

class Address(object):
	def __init__(self, houseNumber, street, city, state, zipCode, apartmentType="", apartmentNum=""):

		self.line1 = "%s %s" % (houseNumber, street)
		self.line2 = "%s %s" % (apartmentType, apartmentNum)
		self.line3 = "%s, %s %s" %(city, state, zipCode)

	def get_lines(self):
		return [self.line1, self.line2, self.line3]

class Phone(object):
	def __init__(self, stringForm, Type):
		self.type = Type
		self.countryCode = stringForm[0]
		self.areaCode = stringForm[1:4]
		self.number = stringForm[4:]

	def get_number(self):
		return "+%s (%s) %s-%s" % (self.countryCode, self.areaCode, self.number[:3], self.number[3:])

class Email(object):
	def __init__(self, Type, address):
		self.type = Type
		self.address = address

def main():

	myBook = AddressBook()

	for i in range(10):
		firstNames = ["bob", "bill"]
		lastNames = ["foo", "bar"]

		randomFName = random.choice(firstNames)
		randomLName = random.choice(lastNames)

		name = Name(fName=randomFName, lName=randomLName)

		monthDays = [1,2,3,4,5,6,7,8,9,10,11,12,13]
		months = ["January", "February"]
		years = [1956, 1957, 1958]

		randomDay = random.choice(monthDays)
		randomMonth = random.choice(months)
		randomYear = random.choice(years)

		dob = DoB(randomDay, randomMonth, randomYear)

		streetNames = ["Oak", "Maple"]
		streetNameEnds = ["St", "Ave"]
		cities = ["San Francisco", "New York", "Chicago"]
		states = ["MA", "CA", "NY", "MI"]
		randomZipCode = "".join([str(random.randint(0,9)) for x in range(5)])

		houseNumber = random.randint(0, 9999)
		randomStreetName = random.choice(streetNames) + " " + random.choice(streetNameEnds)
		randomCity = random.choice(cities)
		randomState = random.choice(states)

		street = Address(houseNumber, randomStreetName, randomCity, randomState, randomZipCode)

		mPhone = Phone("1" + "".join([str(random.randint(0,9)) for x in range(10)]), "Mobile")
		wPhone = Phone("1" + "".join([str(random.randint(0,9)) for x in range(10)]), "Work")

		domains = ["yahoo", "gmail", "hotmail"]
		users = ["XxlifesucksxX", "free2rhyme"]

		randomEmail = "%s@%s.com" % (random.choice(users), random.choice(domains))
		email = Email(randomEmail, "Work")

		myBook.add_person(Person(name, dob, street, mPhone, wPhone, email))

	myBook.sample()

if __name__ == '__main__':
	main()

#"280 Orchard Ave Unit O Mountain View, CA 94043"