from data.WebhookBody import *
from data.Enums import *
from utils.secret_util import *
import requests
from configs.config import *

def deal_callback(payload: PayLoad):
    match payload.op:
        case WebhookOpCode.callback_verify.value:
            return verify_callback_sign(payload.d)
        case WebhookOpCode.dispatch.value:
            return None


# 首次配置回调地址时候平台用来校验签名
def verify_callback_sign(d):
    token = d.get("plain_token")
    event_ts = d.get("event_ts")
    secret = settings.BOT_SECRET
    private_key, public_key, seed = generate_ed25519_keypair_from_secret(secret)
    sign = sign_validation_payload(private_key, event_ts, token)
    res = ValidationRes(
        plain_token=token,
        signature=sign
    )
    return res


def get_access_token():
    url = settings.SIGN_HOST
    data = {
        "appId": settings.BOT_APPID,
        "clientSecret": settings.BOT_SECRET
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        result = response.json()
        return result.get('access_token')
    else:
        print(f"获取access_token失败: {response.text}")
        return None

if __name__ == '__main__':
    res = get_access_token()
    print(res)