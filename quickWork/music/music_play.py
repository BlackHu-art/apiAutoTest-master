# @Time    : 2021/7/29 17:42
# @Author  : hubaba
# @Software: PyCharm
import time

# import AudioSegment as AudioSegment
import playsound

# 音频播放方法一
# song = AudioSegment.from_wav(r"D:\User\Dashujv\语音分析\data\声声慢.wav")
# from pydub.playback import play
#
# play(song)

# 音频播放方法二
import os

file = r"D:\User\Dashujv\语音分析\data\声声慢.wav"
os.system(file)

# 音频播放方法三
playsound(r"D:\WorkSpace-PyCharm\quickWork\music\14321.mp3")

# 音频播放方法四
import pygame

pygame.mixer.init()

track = pygame.mixer.music.load(r"D:\WorkSpace-PyCharm\quickWork\music\14321.mp3")
pygame.mixer.music.play()

pygame.mixer.music.pause()  # 暂停
pygame.mixer.music.unpause()  # 取消暂停
# 成功播放音乐，并有暂停，取消暂停功能。

# 方法五
import winsound

winsound.PlaySound(r"D:\User\Dashujv\语音分析\data\声声慢.wav", winsound.SND_FILENAME)
