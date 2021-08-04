# @Time    : 2021/8/3 10:36
# @Author  : hubaba
# @Software: PyCharm
#  title：爬取视频网站并获取视频播放地址

import re
import requests
from lxml import etree
from selenium import webdriver

BASE_URL = "****"  # 网站地址
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}


#  定义一个类，用于专门爬取页面，得到想要的内容
class Procuder(object):
    driver_path = "填入你的chromedriver.exe的绝对路径"
    driver = webdriver.Chrome(executable_path=driver_path)

    src_and_name = []  # 定义一个列表来放视频的标题和播放地址

    #  定义一个爬取并解析页面的函数，得到要下载视频的url和视频名字
    def get_data(self, url):
        try:
            #  请求首页，得到BASE_URL中槽的数字
            response = requests.get(url, headers=HEADERS)
            response.raise_for_status()
            response.encoding = response.apparent_encoding
            text = response.text
            html = etree.HTML(text)
        except:
            print('爬取首页时出现错误!')

        try:
            lis = html.xpath("//div[@class='box movie_list']/ul/li")  # 解析包含多个视频链接的首页，得到播放视频页与首页的中间页面
            for li in lis:
                video_flase_url = li.xpath(".//a/@href")[0]  # 播放视频页与首页的中间页面的url
                number = re.findall(r'\d+', video_flase_url)[0]  # true_url中槽的数字，从而构造播放页面的url
                true_url = 'BASE_URL/video/{}.html?{}-0-0'.format(number, number)  # 构造播放视频页url

                #  为了拿到视频的title
                true_url_response = requests.get(true_url, headers=HEADERS)
                true_url_response.encoding = true_url_response.apparent_encoding
                true_url_text = true_url_response.text
                true_url_html = etree.HTML(true_url_text)
                video_need_name = true_url_html.xpath("//head/title/text()")[0]
                video_name = re.search(r"_(.*) -", video_need_name).group(1) + '.mp4'  # 视频标题

                #  解决多层iframe嵌套问题，从而拿到视频下载地址
                driver = Procuder.driver  # 使用类变量
                driver.get(true_url)
                iframe = driver.find_elements_by_tag_name('iframe')[0]
                driver.switch_to.frame(iframe)
                iframe2 = driver.find_elements_by_tag_name('iframe')[1]
                driver.switch_to.frame(iframe2)
                text2 = driver.page_source  # xpath和selenium结合使用
                html = etree.HTML(text2)
                video_url = html.xpath("//div[@id='player']/iframe/@src")[0]  # 视频的播放地址
                data = {video_name: video_url}
                Procuder.src_and_name.append(data)

        except:
            print('解析时出现错误!')

    def run(self):
        url = BASE_URL
        self.get_data(url)


def main():
    t = Procuder()
    t.run()
    print(t.src_and_name)


if __name__ == '__main__':
    main()
