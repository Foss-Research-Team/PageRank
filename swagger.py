import requests

res = requests.get('https://stallman.org')

res.raise_for_status()

playFile = open('Stallman.txt','wb')

for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()
