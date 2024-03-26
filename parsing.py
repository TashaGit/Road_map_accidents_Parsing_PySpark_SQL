# pip install lxml
# pip install tqdm
# pip install wget

import os.path
import requests
from lxml import html
from tqdm import tqdm
import wget

os.makedirs('data', exist_ok=True)


def check_file(url):
    geojson_name = url.split('/')[-1]

    if os.path.exists(f'data/{geojson_name}'):
        return True
    else:
        return False


page = requests.get('https://cms.dtp-stat.ru/media/opendata/')
webpage = html.fromstring(page.content)

names = webpage.xpath('//a/@href')[1:]
print('Всего файлов:', len(names))

for i in tqdm(range(len(names))):
      # time.sleep(1)
    if check_file(names[i]) == False:
        url = f'https://cms.dtp-stat.ru/media/opendata/{names[i]}'
        response = wget.download(url, 'data/' + url.split('/')[-1])


