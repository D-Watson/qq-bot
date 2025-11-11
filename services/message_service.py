from data.WebhookBody import *
from data.Enums import *
from utils.secret_util import *


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
    secret = 'VxPrJlEhAd6Z2VzTxRvPtOtOtOtOuQwS'
    private_key, public_key, seed = generate_ed25519_keypair_from_secret(secret)
    sign = sign_validation_payload(private_key, event_ts, token)
    res = ValidationRes(
        plain_token=token,
        signature=sign
    )
    return res
