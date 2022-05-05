#ตอนที่ 4 - สร้าง Series จาก Numpy

import pandas as pd
import numpy as np

data_ls = [10,20,'tao',1.3,"มะม่วง"] 

#สร้างจาก numpy
npdata = np.array(data_ls)

#สรา้ง Series จาก Numpy
ps = pd.Series(npdata) #สร้างจาก numpy
print(ps)

