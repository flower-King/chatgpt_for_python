import os
import openai
import json

openai.api_key = "你的API_KEY"

_目录列表 = []
_对话列表 = []
_一句话 = {}
_当前目录 = os.getcwd()

for _文件名 in os.listdir(_当前目录):
    if _文件名.endswith(".json"):
        _目录列表.append(_文件名.split(".")[0])

if _目录列表 != []:
    print("输入编号继续对话，输入 0 新建聊天：")
    for i in range(len(_目录列表)):
        print(i+1, _目录列表[i])
    inputindex = input("：")
    if inputindex == "":
        exit()
    chatIndex = int(inputindex)-1
    if (inputindex != "0"):
        _对话文件名 = _目录列表[chatIndex]+".json"
        with open(_目录列表[chatIndex]+".json", "r") as f:
            _对话列表 = json.load(f)
        for i in _对话列表:
            if i["role"] != "system":
                if i["role"] == "user":
                    print("我：", i["content"])
                elif i["role"] == "assistant":
                    print("chatGPT：", i["content"])
    else:
        _对话文件名 = input("新建聊天名称：")+".json"
        _对话列表 = [{"role": "system", "content": "你是一个乐于助人并使用中文来对话的助手。"},]
else:
    _对话文件名 = input("新建聊天名称：")+".json"
    _对话列表 = [{"role": "system", "content": "你是一个乐于助人并使用中文来对话的助手。"},]

while True:
    _我发送的消息 = input("我：")
    if _我发送的消息 == "":
        exit()
    _一句话 = {"role": "user", "content": _我发送的消息}
    _对话列表.append(_一句话)
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=_对话列表)
    _chatgpt返回的消息 = completion.choices[0].message["content"]
    print("chatGPT：", _chatgpt返回的消息)
    _一句话 = {"role": "assistant", "content": _chatgpt返回的消息}
    _对话列表.append(_一句话)
    with open(_对话文件名, "w") as f:
        f.write(json.dumps(_对话列表))
