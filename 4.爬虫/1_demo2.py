# !/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
project:41_爬虫
author:lanyu 2020/6/30
"""

class demo():
    """
    1. 调度器 ---》 引擎 ----》 下载中间件 ---> 下载器
    2. 下载发送请求，获取响应 ---下载中间件 --->引擎---》爬虫中间件---》爬虫
    3. 爬虫提取地址，组成请求对象 ---> 爬虫中间件---》引擎---》调度器
    4.爬虫提取数---》引擎 ---》 管道
    5.管道进行数的清洗和保存

    1fc7bbf050f000000.ts
    1fc7bbf050f000001.ts

    1fc7bbf050f001846.ts

    """
    pass

# for i in range(1,1846):
#
#     url  ="https://youku.cdn7-okzy.com/20200517/19513_caa698df/1000k/hls/1fc7bbf050f00{}.ts".format(i)
# # https://youku.cdn7-okzy.com/20200517/19513_caa698df/index.m3u8
# # https://youku.cdn7-okzy.com/20200517/19513_caa698df/index.m3u8
#
# import requests

# 1, 提取资源
import requests
# with open('index.m3u8','wb') as f:
#     f.write(requests.get('https://youku.cdn7-okzy.com/20200517/19513_caa698df/1000k/hls/index.m3u8').content
# )

# 2， 提取媒体文件  ts流


# 3， 拼接请求下载每一个小片段
# for i in file[:5]:
#     print(type(i))
#     import os
#     if os.path.exists('dddd') is False:
#         os.mkdir('dddd')
#     # 1fc7bbf050f000000.ts
#     with open('./dddd/'+i,'wb') as f:                                                         # 1fc7bbf050f000001.ts
#         f.write(requests.get('https://youku.cdn7-okzy.com/20200517/19513_caa698df/1000k/hls/{}'.format(str(i))).content)
#     print(i+"成功")

# 4， 资源合并
# import os
# path = r"E:\output\spider\41_爬虫\day8\dddd"
#
# file_list = os.listdir(path=path)
#
# shell = '+'.join(file_list)
#
# shell = 'copy /b '+ shell + ' sp.mp4' + '\n'+ 'del *.ts'
#
# cwd_path = os.getcwd()
#
# print('*' * 60)
# res = open(cwd_path+'\dddd' + "\sphc.cmd",'w')
# res.write(shell)
# res.close()


import requests
from threading import Thread
import queue


class Mthreads(Thread):
    def __init__(self,queue):
        super(Mthreads,self).__init__()
        self.queue = queue
        self.path = r"E:\output\spider\41_爬虫\day8\dc"

    def run(self):
        self.spiders()

    def spiders(self):
        while not self.queue.empty():
            url = self.queue.get()  # 取值
            import time
            time.sleep(0.5)
            res = requests.get(url)
            file_name = self.path + '\{}' .format(url.split('/')[-1])
            with open(file_name,'wb') as f:
                f.write(res.content)


def main():
    myqu = queue.Queue()
    fs = open('index.m3u8', 'r', encoding='utf-8')
    text = fs.readlines()
    file = []
    for i in text:
        if i.find('#EX') == -1:
            file.append(i.replace("\n", ""))
    fs.close()

    for i in file:
        urls = "https://youku.cdn7-okzy.com/20200517/19513_caa698df/1000k/hls/{}".format(str(i))
        myqu.put(urls)  # 入队

    list_th = []
    for i in range(10):
        mythread = Mthreads(myqu)
        mythread.start()
        list_th.append(mythread)

    for j in list_th:
        j.join()

if __name__ == '__main__':
    main()


