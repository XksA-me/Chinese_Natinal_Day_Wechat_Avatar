# -*- coding: utf-8 -*-
"""
@author = 老表
@date = 2023-09-29
@个人公众号 = 简说Python
@微信号 = pythonbrief
"""


from flask import Flask, render_template, request, send_file, redirect, url_for
import os
import random
from PIL import Image
from io import BytesIO

# 创建上传图片存储路径
basedir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(basedir, 'output')

if not os.path.exists(file_path):
    os.makedirs(file_path)

app = Flask(__name__, static_folder=file_path, static_url_path='/show')

# 过滤非图片文件
def file_filter(filename):
    filter_ = ['png', 'jpg', 'jpeg', 'JPG', 'PNG', 'JPEG']
    return '.' in filename and filename.rsplit('.', 1)[1] in filter_

# 图片合并
def handle_picture(style="01", avatar="./wechat.jpg"):
    '''
    style : 模板文件名称，我是以序号命名的
    avatar : 微信头像文件路径
    '''
    # 打开图片模版
    img1 = Image.open(f"./style/{style}.png")
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
    return img2

# 随机选9个序号
def random_serial():
    serial = [f"0{i}" if i < 10 else str(i) for i in range(13)]
    return random.sample(serial, 9)
    
# 首页 
@app.route('/')
def index():
    return render_template('index.html')

# 图片上传接口
@app.route('/upload', methods=['POST'])
def upload():
    img = request.files['img']
    if img and file_filter(img.filename):
        for style in random_serial():
            handle_picture(style, img)
        return redirect(url_for('shows'))
    else:
        return "上传失败"
                               
# 图片查看接口
@app.route('/shows')
def shows():
    file_list = [i for i in os.listdir(file_path) if file_filter(i)]
    return render_template('shows.html', data=file_list)
    
# 下载图片接口
@app.route('/download/<filename>', methods=['GET'])
def download(filename):
    file_list = [i for i in os.listdir(file_path) if file_filter(i)]
    if filename in file_list:
        img = Image.open(file_path + "/" + filename)
        output_stream = BytesIO()
        img.save(output_stream, format='PNG')
        output_stream.seek(0)
        return send_file(output_stream, mimetype='image/png', as_attachment=True, download_name=f'downloaded_{filename}')
    else:
        return "File not found.", 404
    


if __name__ == '__main__':
    # run，指定 host 和 port
    app.run(host='0.0.0.0', port=7860, debug=True)

    
    