# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 15:26:35 2018

@author: yutaro
"""

# ループで合計を計算しよう

points = {"国語" : 70, "算数" : 35, "英語" : 52}
sum = 0
# この下で、辞書の値の合計をループで計算してみよう
for i in points:
    sum = sum + points[i]
print(int(sum))
