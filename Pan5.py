#ตอนที่ 7 - การเข้าถึงข้อมูลใน Series

import pandas as pd

#ข้อมูลชนิด dict
data = {"องุ่น":50,'กล้วย':30,'มะละกอ':30} 
data = pd.Series(data)
    #เข้าถึงข้อมูลเเบบ ใช้ key
print(data['องุ่น'])

print(data['กล้วย'])

print()

#การเข้าถึงแบบโดยใช้งานเลข index
dnum = [10,20,30,40]
a = pd.Series(dnum)

print(a[1])

