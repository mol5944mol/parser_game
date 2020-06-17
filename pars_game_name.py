import requests
from bs4 import BeautifulSoup
from os.path import exists
from os import remove

output = input('output_file: ')

if exists(output):
    isdel = input('A file with that name already exists, delete it and create a new one? [y/n]: ').lower()
    if isdel == 'yes' or isdel == 'y':
        remove(output)
    else:
        quit()

def get_gamename(url):
    try:
        resp = requests.get(url,headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/81.0.4044.138 Chrome/81.0.4044.138 Safari/537.36'})
        soup = BeautifulSoup(resp.text,'html.parser')
        with open(output,'at') as file:
            for i in soup.find('div',class_='games-list border-10 shadow').find_all('a'):
                name_game = i.select('h2')[0].get_text()
                print(name_game)
                file.write(name_game + '\n')
    except:
        pass

resp = requests.get('http://vseigru.net/',headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/81.0.4044.138 Chrome/81.0.4044.138 Safari/537.36'})
soup = BeautifulSoup(resp.text,'html.parser')

for i in soup.find_all('a'):
    link = i.get('href')
    if link != '/':
        get_gamename("http://vseigru.net" + link)

    if '/?start' in link:
        break
