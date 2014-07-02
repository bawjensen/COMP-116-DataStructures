import random

class BaseURL(object):
	def __init__(self, website):
		self.base = website
		self.page = WebPage()
		self.url = ""
		self.location = 0

	def link(self):
		

	def back(self):
		pass

	def forward(self):
		pass



class WebPage(object):
	def __init__(self, link):
		self.name = self
		link.linksList = []

	def add_links(self, linksList):
		for link in linksList:
			self.linksList.append(WebPage(link))


def main():
	website = BaseURL("http://www.wheatoncollege.edu/")

	mainLinks = ["Admission", "Academics", "Campus Life", "News & Events", "Athletics"]

	website.page.add_links(mainLinks)
	names = ["faculty", "academics", "majors-minors", "majors", "minors", "profiles"]

	baseURL = "http://www.wheatoncollege.edu/"

	choices = ["back", "forward", "link"]

	for i in range(100000):
		choice = random.choice(choices)

		if choice == "back":
			extraList = extraURL.split("/")

			extraURL = "".join(map(str,extraList[:-1]))

		if choice == "forward":
			pass


if __name__ == '__main__':
	main()