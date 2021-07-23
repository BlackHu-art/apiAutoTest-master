# @Time    : 2021/7/20 16:52
# @Author  : hubaba
# @Software: PyCharm
import requests
from requests import RequestException
from pyquery import PyQuery as pq
import time
import threading
import queue
import random

queueLock = threading.Lock()
workQueue = queue.Queue(10)
exitFlag = 0
threads = []
urlList = ['https://blog.csdn.net/DrMaker/article/details/118907835?spm=1001.2014.3001.5501']
# urlList = ['https://blog.csdn.net/DrMaker?spm=1001.2100.3001.5343']

cookie = ['', ''
          ]
Agent = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
    'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)',

    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36',

    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36',
    'Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) Apple'

]


# 获取博主所有博客的属性信息。
def get_url(url):
    urlBuf = []
    # 模拟浏览器，不用改，几乎固定
    headers = {
        'User-Agent': Agent[0],
        'cookie': cookie[0]
    }

    # 模拟点击网址
    html = requests.get(url, headers=headers, verify=True).text
    # 解析代码
    doc = pq(html)
    # 调试
    # print(doc)

    # 点击CSDN右上角头像“我的博客”，在我的博客界面
    # 右键查看源代码找到博客相关信息

    # 获取class为article-item-box的代码
    a = doc('.article-item-box')

    for item in a.items():
        # 调试
        # print(item)

        # 从上面获取的代码中获取博客属性信息。
        # 标题
        # 一开始没准备爬标题和浏览量，本来应该用正则表达式
        # 这里直接把相关信息按照标签">"拆开后在列表取出来
        title = item('.article-type')
        title = str(title)
        title = title.split('>')[-1]
        title = item('.article-type')
        title = str(title)
        title = title.split('>')[-1]
        title = title.replace(' ', '')
        print('标题  ： ' + title)
        # 浏览量
        readnum = item('.read-num')
        readnum = str(readnum)
        readnum = readnum.split('>')[2]
        readnum = readnum.split('<')[0]
        print('浏览量： ' + readnum)
        # 回车
        # print('\n')
        # URL
        b = item.find('a').attr('href')
        # 把URL写到列表中
        urlBuf.append(b)
    print('\n')
    return urlBuf


# 对URL进行访问
def get_page(url):
    try:
        # for a in Agent:
        for a in range(4):

            headers = {
                'Referer': 'https://blog.csdn.net',  # 伪装成从CSDN博客搜索到的文章
                'User-Agent': Agent[random.randint(0, len(Agent) - 1)],  # 伪装成浏览器
                # 'User-Agent':a,
                'cookie': cookie[random.randint(0, len(cookie) - 1)]

            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                ab = 0

                # return response.text

            # return None
    except RequestException:
        print('请求出错')
        return None


class myThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    # 访问博客
    def fun(threadID):
        while True:
            for a in urlList:
                get_page(a)
                # 打印浏览量信息
            get_url(url)

            # 等待60~70s重新刷新
            time.sleep(random.randint(10, 15))
            print('博客 ' + str(threadID) + ' 已刷新')

    # 线程任务
    def run(self):

        print("开启线程：" + self.name)
        # 执行fun
        myThread.fun(self.threadID)
        process_data(self.name, self.q)
        print("退出线程：" + self.name)


def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)


# 开启线程
def start(num):
    # for i in range(0,num):
    for i in range(0, 3):
        thread = myThread(i, i, workQueue)
        thread.start()
        threads.append(thread)
        time.sleep(0.5)


# ！！！修改为自己博客的网址！！！
url = 'https://blog.csdn.net/DrMaker?spm=1001.2100.3001.5343'


def main():
    # 先执行get_url获取一下博客的URL写到urllist中
    urlList.extend(get_url(url))
    # 博客的数量等于URL的数量
    for a in urlList:
        print('\'' + a + '\',')
    num = len(urlList)
    print('您一共有 ' + str(num) + ' 篇博客')

    # 开启线程，执行访问任务。
    start(num)


if __name__ == '__main__':
    main()
