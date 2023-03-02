# Chatgpt_for_python
Use the ChatGPTAPI to open a dialogue on the console with PyThon. You can save the dialogue. You can continue the dialogue.
## installation method:
```shell
PIP Install -Force -Reinstall -v "Openai == 0.27.0"
```
You need to configure openai.api_key
```python3
openai.api_key = "Your API_KEY"
```
## How to use:
```shell
python3 main.py
```
After the new chat will generate the chat content of the same name JSON file in the current directory, and the dialogue will be over directly.
### Notice:
Chatgpt's API seems to be a wall now, you can use Proxychains to open the agent
```shell
proxychains python3 main.py
```
## Effect:
![image](https://user-images.githubusercontent.com/60785775/222438502-48ba69de-13ee-4996-911c-16943c3258e5.png)

![image](https://user-images.githubusercontent.com/60785775/222438701-cf67226b-828e-43fd-b05f-1a8eb9ef891d.png)
