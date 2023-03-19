# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 16:32:40 2023

@author: Andreas J. P.
"""

import re

re_champlist = re.compile(r'=(\[\{_id:"[^{}]+championId:".+?\}\])')

with open("app.fbd7eb26.js", encoding="UTF-8") as file:
    js = file.read()
    champlist = re_champlist.findall(js)[0]

with open("loldle-champ-data.js", "w") as file:
    file.write(champlist)
