# -*- coding: utf-8 -*-
s = "The Manhattan campus of Fordham Gabelli Business School is located near the Lincoln Center"
s1 = s.lower()
a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
y = 0
x = []
for y in range(26):
    if s1.count(a[y]) > 0: 
        x.append((a[y] , s1.count(a[y])))
    else: continue
    y += 1
print('x=', x)
