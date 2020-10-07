# -*- coding: utf-8 -*-
import requests

res = requests.get("https://www.yandex.ru/").text
print(res)
