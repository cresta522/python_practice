import numpy as np

def inner(a, b, c, d):
    x = np.array([a, b])
    y = np.array([c, d])
    ans = np.dot(x, y)
    
    print(ans)
    
inner(1, 2, 4, 3)