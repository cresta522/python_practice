'''

4 つの数 a, b, c, d を受け取り, ベクトル (a, b) と (c, d) の内積を計算する関数, 
inner(a, b, c, d) を書き, 適当な例を使って確かめよ.


'''

import numpy as np

def inner(a, b, c, d):
    x = np.array([a, b])
    y = np.array([c, d])
    ans = np.dot(x, y)
    
    print(ans)
    
inner(1, 2, 4, 3)