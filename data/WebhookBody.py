from pydantic import BaseModel


class PayLoad(BaseModel):
    id: str
    op: int
    d: dict
    s: int  # 下行消息都会有一个序列号，标识消息的唯一性，客户端需要再发送心跳的时候，携带客户端收到的最新的s
    t: str


class PayLoadData(BaseModel):
    plain_token: str
    event_ts: str


class ValidationRes(BaseModel):
    plain_token: str
    signature: str
