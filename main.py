#!/usr/bin/python3

import json
import requests

api_url = 'http://api.migu.jsososo.com/search?keyword='


def color(strings, option=True):
    if option is False:
        return "\033[31m{}\033[0m".format(strings)
    else:
        return "\033[4;33m{}\033[0m".format(strings)


def search(name):

    dic = {}
    r = requests.get(api_url+name)
    music_list = json.loads(r.text)
    if music_list.get('result') == 100:
        print('ok')
        music_list_data = music_list.get('data')
        music_list_data_list = music_list_data.get('list')
        for index, li in enumerate(music_list_data_list, start=1):
            # print(li)
            data_album = li.get('album')
            album_name = data_album.get('name')
            album_name_artists_name = li.get('artists')[0].get('name')
            print(color(index), '<>', album_name_artists_name, li.get('name'),
                  '《{}》'.format(color(album_name)))
            dic['{}-{}'.format(li.get('name'), album_name)] = li.get('url')
        return dic
    else:
        return None


def download(file, url):
    print('downloading...')
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open('{}.mp3'.format(file), 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                f.write(chunk)
    print('download complate')
    return None


while True:
    while True:
        name = input('Input music name:')
        if name != '':
            break
        else:
            print('input error')
    name_info = search(name)
    while True:
        choose_id = input('Input download id:')
        try:
            choose_id = int(choose_id)
            while True:
                if choose_id > len(name_info):
                    print('error download id')
                else:
                    break
            break
        except ValueError:
            print('error download id')
    for index, i in enumerate(name_info, start=1):
        if choose_id == index:
            download(i, name_info[i])
