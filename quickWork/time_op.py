# @Time    : 2021/7/29 18:15
# @Author  : hubaba
# @Software: PyCharm
# @Description : 程序运行时间和得到cpu时钟时间（后者更更精确）

import datetime

# 第一种
start = datetime.datetime.now()
# 此处插入运行代码
end = datetime.datetime.now()
# 输出程序运行时间
print(end - start)

import time

# 第二种
start = time.clock()
# 此处插入运行代码
end = time.clock()
# 输出运行时间
print(end - start)
