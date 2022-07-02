import rawpy
from matplotlib import pyplot as plt 

fpath = 'test.dng'

with rawpy.imread(fpath) as raw:
  plt.imshow(raw.raw_image)
  plt.show()