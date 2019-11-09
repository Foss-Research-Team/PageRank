import bs4


exampleFile = open('example.html')

exampleSoup = bs4.BeautifulSoup(exampleFile.read(),'html.parser')

elems = exampleSoup.select('#author')

print(type(elems)) #elems is a list of Tag objects

print(len(elems))

print(type(elems[0]))

print(str(elems[0]))

print(elems[0].getText())

print(elems[0].attrs)
