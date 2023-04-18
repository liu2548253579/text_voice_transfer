# 语音转文字与文字转语音实现

## 1.安装

确保你所处的操作系统已安装ffmpeg、python版本大于或等于3.8

然后cd到工程目录下

安装所需依赖：

```bash
pip install -r requirements.txt
```

## 2.配置百度API

去[百度AI官网](https://ai.baidu.com/?track=cp:ainsem|pf:pc|pp:tongyong-pinpai|pu:pinpai-baiduAI|ci:|kw:10003812)主策并申请语音识别的API勾选文字转语音和语音转文字功能获取到**APP_ID、API_KEY**与**SECRET_KEY**并将其填写到**baidu_api.txt**

例如：

```bash
APP_ID:123456789
API_KEY:xxxxxxxxxxxxxxxxxxx
SECRET_KEY:xxxxxxxxxxxxxxx
```

## 3.开始使用

打开终端输入如下指令即可开始使用

```
python main.py
```

根据提示可以录入声音并转化为文字，而后将文字转化为合成语音。
