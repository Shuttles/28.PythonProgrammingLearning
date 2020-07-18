#!/usr/bin/env python
# coding=utf-8

import requests

src = "https://imgsa.baidu.com/forum/w%3D580/sign=5ed52b8e2adda3cc0be4b82831e83905/f66fc65c10385343ee1135309713b07ecb80888e.jpg"
response = requests.get(src)
with open("./data/tieba/images/1.Kobe", "wb") as file:
    file.write(response.content)
