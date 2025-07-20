from fileinput import filename

import requests

text = 'Всем пока'
url = f'https://cataas.com//cat/says/{text}'
response = requests.get(url)
print(response.headers)
content_length = response.headers['Content-Length']
content_type = response.headers['Content-Type']
date = response.headers['Date']

with open('goodbye.jpg', 'wb') as f:
    f.write(response.content)

import json
data_about_image = {
'Content-Length': content_length,
'Content-Type': content_type,
'Date': date
}

with open("data_about_image.json", "w") as json_file:
    json.dump(data_about_image, json_file, indent=4)


import configparser
config = configparser.ConfigParser()
config.read('settings.ini')
yd_token = config['tokens']['ya_disc']

url_create_folder = 'https://cloud-api.yandex.net/v1/disk/resources'
params = {
    'path': 'PD-FPY-SPD-130'
}
headers = {
    'Authorization': f'OAuth {yd_token}'
}
response = requests.put(url_create_folder,
                        params=params,
                        headers=headers)

url_upload_link = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
params = {
    'path': 'PD-FPY-SPD-130/goodbye.jpg',
    'overwrite': 'true'
}
response_up = requests.get(url_upload_link,
                        params=params,
                        headers=headers)
print(response_up.json())
url_upload = response_up.json()['href']

with open('goodbye.jpg', 'rb') as f:
    requests.put(url_upload, files={'file': f})