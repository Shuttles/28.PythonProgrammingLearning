#!/usr/bin/env python
# coding=utf-8
import re

str = '<img class="BDE_Image" src="http://tiebapic.baidu.com/forum/w%3D580/sign=ed672db0a5fb43161a1f7a7210a44642/8f4d6e061d950a7bd20203bf1dd162d9f2d3c958.jpg" size="117679" changedsize="true" width="560" height="929" style="cursor: url(&quot;//tb2.bdstatic.com/tb/static-pb/img/cur_zin.cur&quot;), pointer;">'


urls = re.findall(r'<img class="BDE_Image".*?src="(.*?)".*?', str)
print(urls)

str1 = '<a href="//tieba.baidu.com/f?kw=%E7%A7%91%E6%AF%94&amp;ie=utf-8&amp;pn=50" class="next pagination-item ">下一页&gt;</a>'
urls = re.findall(r'<a href="(.*?)".*?>下一页&gt;</a>', str1)
print(urls)
