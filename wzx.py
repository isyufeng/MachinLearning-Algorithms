# coding:utf-8
import requests
import json
query = '王祖贤'
''' 下载图片'''

def download(src, id):
    dir = './' + str(id) + '.jpg'
    try:
        pic = requests.get(src,timeout=10)
    except requests.exceptions.ConnectionError:
        print ('图片无法下载')
    fp = open(dir,'wb')
    fp.write(pic.content)
    fp.close()

for i in range(0,22598,20):
    url = 'https://www.douban.com/j/search_photo?q='+ query + '&limit=20&start=' + str(i)
    html = requests.get(url).text
    response = json.loads(html,encoding='utf-8')
    for image in response['images']:
        print image['src']
        download(image['src'],image['id'])


