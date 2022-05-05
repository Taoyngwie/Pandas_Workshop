#สร้าง Series กำหนด Index

import pandas as pd

item = ["กล้วย","มะม่วง","ส้ม"] 

idx = [50,20,30]


#สรา้ง Series จาก Numpy
ps = pd.Series(item,index=idx) #สร้างจาก numpy
print(ps)

