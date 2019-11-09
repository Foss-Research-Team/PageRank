import bs4

exampleFile = open('example.html')

exampleSoup = bs4.BeautifulSoup(exampleFile.read(),'html.parser')

pElems = exampleSoup.select('p')

print(str(pElems[0]))

print(pElems[0].getText())

print(str(pElems[1]))

print(pElems[1].getText())

print(str(pElems[2]))

print(pElems[2].getText())
