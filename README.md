# chatgpt_for_python
使用chatgptAPI用python在控制台开启对话，可保存对话，可继续对话，可连续对话。
## 安装方式：
```shell
pip install --force-reinstall -v "openai==0.27.0"
```
需要配置openai.api_key，默认会去读取OPENAI_API_KEY这个环境变量的值，
嫌麻烦可以直接在代码中设置api_key
```python3
openai.api_key = "你的API_KEY"
```
## 使用方式：
```shell
python3 main.py
```

### 注意：
chatGPT的API现在好像被墙了，可以使用proxychains开启代理
```shell
proxychains python3 main.py
```
