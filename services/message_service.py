import zai
from zai import ZhipuAiClient
print(zai.__version__)


client = ZhipuAiClient(
    api_key="3e0e41c3dd96436f8822f548ea360144.FWv8cCeCjGBYBG1e"
)
response = client.chat.completions.create(
    model="glm-4.6",
    messages=[
        {
            "role": "system",
            "content": "你是一个有用的AI助手。"
        },
        {
            "role": "user",
            "content": "你好，请介绍一下自己。"
        }
    ],
    temperature=0.6
)

# 获取回复
print(response.choices[0].message.content)