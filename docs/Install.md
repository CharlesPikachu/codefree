# 安装codefree


#### 环境配置

- 操作系统: Linux or macOS or Windows
- Python版本: Python3.6+


#### PIP安装(推荐)

在终端运行如下命令即可(请保证python在环境变量中):

```sh
pip install codefree --upgrade
```


#### 源代码安装

**1.在线安装**

运行如下命令即可在线安装:

```sh
pip install git+https://github.com/CharlesPikachu/codefree.git@master
```

**2.离线安装**

利用如下命令下载codefree源代码到本地:

```sh
git clone https://github.com/CharlesPikachu/codefree.git
```

接着, 切到codefree目录下:

```sh
cd codefree
```

最后运行如下命令进行安装:

```sh
python setup.py install
```