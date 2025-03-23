# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 16:44:22 2025

@author: HP
"""

import random as r
#son = r.randint(50,100)
#print(son)

# choice
ismlar = ['ali', 'vali', 'hasan', 'husan']
ism = r.choice(ismlar)
print(ism)
print(r.choice(ism))

# shuffle
x = list(range(10,100))
print(x)
r.shuffle(x)
print(x)