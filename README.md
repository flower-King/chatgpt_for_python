# chatgpt_for_python
[English](https://github.com/flower-King/chatgpt_for_python/blob/main/README.en.md "English")

使用chatgptAPI用python在控制台开启对话，可保存对话，可继续对话，可连续对话。
## 安装方式：
```shell
pip install --force-reinstall -v "openai==0.27.0"
```
需要在代码中配置openai.api_key
```python3
openai.api_key = "你的API_KEY"
```
## 使用方式：
```shell
python3 main.py
```
在新建聊天后会在当前目录生成同名json文件记录聊天内容，直接回车结束对话。
### 注意：
chatGPT的API现在好像被墙了，可以使用proxychains开启代理
```shell
proxychains python3 main.py
```
## 效果：
![image](https://user-images.githubusercontent.com/60785775/222438502-48ba69de-13ee-4996-911c-16943c3258e5.png)

![image](https://user-images.githubusercontent.com/60785775/222438701-cf67226b-828e-43fd-b05f-1a8eb9ef891d.png)

