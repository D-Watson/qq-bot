from enum import Enum


class WebhookOpCode(Enum):
    # 接收用户消息
    dispatch = 0
    # 我收到平台消息时候返回ack
    reply = 12
    # 初次配置的时候平台校验
    callback_verify = 13
