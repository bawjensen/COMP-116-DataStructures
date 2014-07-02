import urllib2
from bs4 import BeautifulSoup
import random
"""
page = urllib2.urlopen("http://www.wheatoncollege.edu/president")

soup = BeautifulSoup(page)

wheatonLinks = []

wheatonLinks.extend([link["href"][1:] for link in soup.findAll('a', href=True) if link["href"][0] == '/'])

wheatonLinks = filter(None, wheatonLinks)

for link in wheatonLinks:
	print link

for link in soup.findAll('a', href=True):
	print link["href"]
"""

class Website(object):
	def __init__(self, s):
		self.baseURL = s

		self.mainPage = Webpage(self.baseURL)

		self.mainPage.constructPage()


class Webpage(object):
	def __init__(self, baseURL, extraURL=""):
		self.baseURL = baseURL
		self.url = baseURL + extraURL
		self.pageConstructed = False

	def constructPage(self, b=5, d=0):
		soupedPage = BeautifulSoup(urllib2.urlopen(self.baseURL))

		self.links = []
		self.links.extend([link["href"][1:] for link in soupedPage.findAll('a', href=True) if link["href"][0] == '/'])
		self.links = filter(None, self.links)

		self.pages = []
		for link in self.links:
			self.pages.append(Webpage(self.baseURL, link))

		self.pageConstructed = True

	def __str__(self):
		return self.url

	def choose_random_link(self):
		return random.choice(self.pages)


class BrowserSimulator(object):
	def __init__(self, website):
		self.website = website
		self.currentPage = website.mainPage
		self.history = []

	def run(self, n):
		for i in range(n):
			self.history.append(self.currentPage)
			self.currentPage = self.currentPage.choose_random_link()
			if not self.currentPage.pageConstructed:
				self.currentPage.constructPage()


def main():
	browSim = BrowserSimulator(Website("http://www.wheatoncollege.edu/"))

	browSim.run(10)

	print [str(page) for page in browSim.history]
	print browSim.currentPage

if __name__ == '__main__':
	main()