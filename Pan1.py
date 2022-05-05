#ตอนที่ 3 - สร้าง Series จาก List & Tuple

import pandas as pd

data_ls = [10,20,'tao',1.3,"มะม่วง"] 
data_tp = (10,20,'tao',1.3,"มะม่วง") 

#สรา้ง Series
ps = pd.Series(data_ls) #สร้างจาก list
print(ps)

ps = pd.Series(data_tp) #สร้างจาก tuple
print(ps)