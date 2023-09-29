# -*- coding: utf-8 -*-
"""
@author = 老表
@date = 2019-09-24
@last = 2023-09-25
@个人公众号 : 简说Python
"""


from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

"""
需求：给图片右下角添加中国国旗
欢迎国庆，喜庆74周年
"""

# 图片合并
def handle_picture(style="01", avatar="./wechat.jpg"):
    '''
    style : 模板文件名称，我是以序号命名的
    avatar : 微信头像文件路径
    '''
    # 打开图片模版
    img1 = Image.open(f"./img/{style}.png")
    img1 = img1.convert('RGBA')
    # 打开原来的微信头像
    img2 = Image.open(avatar)
    img2 = img2.convert('RGBA')
    if img1.size > img2.size:  # 判断图片大小，统一改为 size 小的尺寸
        # 修改图片尺寸
        size = img2.size
        img1.thumbnail(size)
    else:
        # 修改图片尺寸
        size = img1.size
        img2.thumbnail(size)
    # 图片粘贴选区
    loc = (0, 0) + size
    # 将img1 粘贴到 img2
    img2.paste(img1, loc, img1)
    img2.save(f"output/new_{style}.png")   # 保存生成的头像图片


avatar = input("请输入微信原头像路径：")
for i in range(12):
    if i < 10:
        i = f"0{i}"
    handle_picture(i, avatar)
print("处理完成，请进入项目目录 output 文件夹下查看！")