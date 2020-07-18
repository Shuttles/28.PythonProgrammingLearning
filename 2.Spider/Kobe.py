#!/usr/bin/env python
# coding=utf-8
'''爬取Kobe百度贴吧前3页的帖子标题和里面的图片'''

import requests

url = "https://tieba.baidu.com/f?kw=%E7%A7%91%E6%AF%94&ie=utf-8&pn=0"

cnt = 1

for i in range(3):
    #对本页进行操作
    response = requests.get(url)
    urls = response.xpath("//div[@class='threadlist_title pull_left j_th_tit']/a/@href").extract()[0] #获取本页中所有帖子的url
    #对本页中所有帖子进行操作
    for u in urls:
        r = response.get(url)
        #获取标题
        title = r.xpath("//div[@class='core_title core_title_theme_bright']/h1/text()").extract()[0]
        with open("./data/tieba/title", "wb") as file:
            file.write(title + '\n')

        #获取图片
        pics = r.xpath("//d_post_content j_d_post_content  clearfix/img/@src").extract()[0]
        for pic in pics:
            with open("./data/tieba/images/{}".format(cnt), "wb") as file:
                file.write(pic.content)
                cnt += 1
    
    #获取下一页url
    url = response.xpath("//div[@id='frs_list_pager']/a[@class='next pagination-item']/@href").extract()[0]
