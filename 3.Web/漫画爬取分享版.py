import requests, os, time
comic_id = input('请输入漫画id（可以用108053测试程序）')
# comic_id = 108053
comicInfoUrl = "https://www.manhuatai.com/api/getComicInfoBody"
param = {
    'product_id': '2',
'productname': 'mht',
'platformname': 'pc',
'comic_id': comic_id
}

sess = requests.session()
sess.headers = {
    'referer': 'https://www.manhuatai.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36 Edg/80.0.361.109'
}

r = sess.get(comicInfoUrl, params=param)
dc = r.json()

comicName = dc['data']['comic_name'].strip()
#创建漫画文件夹
path = './' + comicName
if not os.path.exists(path):
    os.mkdir(path)

#遍历所有章节
ls = dc['data']['comic_chapter']
ls.reverse()
for item in ls:
    base_url = 'https://mhpic.jumanhua.com'
    # base_url = 'https://mhpic.dm300.com'
    jpg_url_0 = base_url + item['rule']

    #创建章节文件夹
    chapter_path = './' + comicName + '/' +item['chapter_name']
    if not os.path.exists(chapter_path):
        os.mkdir(chapter_path)

    # path = './' + comicName+item['chapter_name']
    print(item['chapter_name'])
    start_num = item['start_num']
    end_num = item['end_num']

    for i in range(start_num, end_num + 1):
        jpg_url = jpg_url_0.replace('$$', str(i)) + '-mht.middle.webp'

        print(jpg_url)
        # break
        local_path = chapter_path + '/%d.jpg'%i

        #断点维护
        if os.path.exists(local_path):continue

        r = sess.get(jpg_url)
        time.sleep(2)
        with open(local_path, 'wb') as f:
            f.write(r.content)