#!/usr/bin/env python
# coding=utf-8

import re

#pattern = r'mr_\w+'
#string = 'MR_hello mr_nihao'
string = """
    <img class="BDE_Image" src="http://tiebapic.baidu.com/forum/w%3D580/sign=ed672db0a5fb43161a1f7a7210a44642/8f4d6e061d950a7bd20203bf1dd162d9f2d3c958.jpg" size="117679" changedsize="true" width="560" height="929" style="cursor: url(&quot;//tb2.bdstatic.com/tb/static-pb/img/cur_zin.cur&quot;), pointer;">
"""
string = """
<a rel="noreferrer" href="/p/6461745356" title="R.I.P" target="_blank" class="j_th_tit ">R.I.P</a>
"""

pattern = r'<a rel="noreferrer" href=".*" title="(.*)" target="_blank" class="j_th_tit ">.*</a>'


print(re.findall(pattern, string))
