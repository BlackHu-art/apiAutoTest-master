# @Time    : 2021/7/29 17:57
# @Author  : hubaba
# @Software: PyCharm
# @Script  : 生成8位数密码文本
import itertools as its
import datetime

# 记录程序运行时间
import winsound

start = datetime.datetime.now()
# 根据此类生成8位密码库
# words = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM.-+*/~!@#$%^&*()'
# words = '.-+*/~!@#$%^&*()'
# words = 'QWERTYUIOPLKJHGFDSAZXCVBNM'
# words = 'qwertyuiopasdfghjklzxcvbnm'
words = '1234567890'
# 控制生成密码位数
r = its.product(words, repeat=8)
dict = open(r'D:\WorkSpace-PyCharm\quickWork\wifi_op\mima.txt', 'a')
for i in r:
    dict.write(''.join(i))
    dict.write(''.join('\n'))
    print(i)

dict.close()
end = datetime.datetime.now()
winsound.PlaySound(r"D:\WorkSpace-PyCharm\quickWork\music\14321.mp3", winsound.SND_FILENAME)

print("密码生成完毕,生成时长：{} Write to ... mima.txt".format(end-start))
