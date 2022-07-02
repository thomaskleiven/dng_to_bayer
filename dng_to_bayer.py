import numpy as np
from matplotlib import pyplot as plt 

width, height = (3280, 2464)

fpath = 'test.dng'
data = np.fromfile(fpath, dtype=np.uint8)
