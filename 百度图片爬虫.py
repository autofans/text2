import requests
import re
import time


class Spider(object):
    """创建一个爬虫类"""
    def __init__(self):  # 初始化对象

        self.key_word = key_word

        self.begin_page = begin_page

        self.file = 1

        self.header = {"User-Agent": "Mozilla/5.0 "
                                "(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                                "(KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}

    def im_spider(self):
        """百度是动态加载图片，必须找到JSON文件再构造URL"""
        for i in range(1, self.begin_page+1):
            p = (i-1)*30
            url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result" \
                  "&queryWord=%s&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=" \
                  "&word=%s&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=" \
                  "&force=&cg=girl&pn=%d&rn=30&gsm=&1572199209381=" % (self.key_word, self.key_word, p)
            # print(url)

            res = requests.get(url, headers=self.header).text
            # print(res)

            ret = re.findall('"middleURL":"(.*?)"', res)
            # print(len(ret))
            for x in ret:
                # print(x)
                self.write_image(x)

    def write_image(self, x):
        """创建写入图片到本地的函数"""
        print("正在爬取第%d张图片......." % self.file)

        img = requests.get(x, headers=self.header).content
        file = open(r"C:\Users\autof\Desktop\百度图片\\%s.jpg" % self.file, "wb")
        file.write(img)
        file.close()
        self.file += 1
        time.sleep(2)


if __name__ == "__main__":
    """执行main方法，创建爬虫对象"""

    key_word = str(input("请输入要搜索的关键词："))
    begin_page = int(input("请输入要爬取的页数："))
    my_spider = Spider()
    my_spider.im_spider()
