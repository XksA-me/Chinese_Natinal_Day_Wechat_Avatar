# 项目说明

## 项目目录
```bash
.
├── README.md  使用说明
├── script     脚本代码
│   ├── code.ipynb   notebook 代码，全流程（获取素材到图片融合）
│   ├── code.py      py 脚本代码
│   ├── img          模版素材图片
│   └── output       存储生成好的微信头像图片目录
├── webui
│   ├── webui.py     webui 项目源码
│   ├── output       存储生成好的微信头像图片目录
│   ├── style        模版素材图片
│   └── templates    前端页面源码
└── wechat.jpg
```

## 更多拓展

我创建了个 Python 应用交流群，如果你感兴趣可以扫下方二维码添加我微信申请加入（备注申请原因）。

<center>
<img src="./wx.png" width=40% />
<p>扫码即可加我微信</p>
</center>


## 环境配置

```bash
# webui
pip install flask Pillow 
# script
pip install requests Pillow matplotlib numpy 
```

## 运行项目

- script

```bash
# code.ipynb 打开后可以直接运行

# code.py 运行
python code.py 
# 输入 微信头像图路径 即可自动处理图片
```

- webui
```bash
python webui.py
```
运行后访问 localhost:7860 或者 服务器ip:7860 即可访问。

具体教程请关注公众号：简说Python 查看。

## 支持与鼓励

点个 start ，参与项目贡献（issue: 提出运行问题、fork: 基于项目实现其他应用）。
