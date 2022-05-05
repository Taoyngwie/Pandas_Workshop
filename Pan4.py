#ตอนที่ 6 - สร้าง Series จาก Dictionary

import pandas as pd

#ข้อมูลชนิด dict
data = {"green":"กล้วย",'red':"มะม่วง",'yellow':"ส้ม"}

#สร้าง Series
ps = pd.Series(data)
print(ps)








