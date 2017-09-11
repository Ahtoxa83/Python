import re
import requests
from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url)
    return response

def save_image(name, link):
	with open (name, 'wb') as f:
		f.write(link.content)

url = "https://www.flickr.com/search/?text=cats"
soup = BeautifulSoup (get_html(url).text, 'lxml')


if get_html(url).status_code != 200:
	print ("Error! Status code =", (url).status_code)

result = soup.find_all("div", class_="photo-list-photo-view")

for n, i in enumerate(result):
	i = i.get("style")
	url_img = re.compile(r'url\(.*\)').findall(i)
	for c in url_img:
		raw_link = c.replace('url(//', '').replace(')', '') # Очищаем ссылку от ненужных символов 
		# (Как вариант хотел очистить регулярными (url\(\/\/)(.*)(\)), но пока не понял как)
		split_raw_link = raw_link.split('/') # Разбиваем строку, чтобы вытащить расширения
		extension = split_raw_link[-1].split('.') # Вытаскиваем расширение из имени файла
		clear_ext = extension[-1] # Собираем расширения
		name = "cat" + str(n) + "." + clear_ext
		img_link = r"https://" + raw_link
		link = requests.get(img_link)
		save_image (name, link)