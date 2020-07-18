#!/usr/bin/env python
# coding=utf-8

import re

str1 = '<a rel="noreferrer" href="/p/6461745356" title="R.I.P" target="_blank" class="j_th_tit ">R.I.P</a>'

str2 = '<a rel="noreferrer" href="/p/6819763349" title="NBA也快开始了 虽然资金不多 买了件便宜的 但也是为老大而" target="_blank" class="j_th_tit ">NBA也快开始了 虽然资金不多 买了件便宜的 但也是为老大而</a>'

pattern = re.compile(r'<a rel="noreferrer" href="(/p/\d+?)" title=".+?" target="_blank" class="j_th_tit .*?">(.+?)</a>')
url_title = pattern.findall(str1)
print(url_title)

for url, title in url_title:
    print("url = ", url)
    print("title = ", title)
