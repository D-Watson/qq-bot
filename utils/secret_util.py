import hashlib
import binascii
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519


def generate_ed25519_keypair_from_secret(bot_secret: str):
    """根据 Bot Secret 生成 Ed25519 密钥对"""
    # 对 Bot Secret 进行哈希得到 32 字节 seed
    seed = hashlib.sha256(bot_secret.encode()).digest()

    # 使用 seed 生成私钥
    private_key = ed25519.Ed25519PrivateKey.from_private_bytes(seed)

    # 获取公钥
    public_key = private_key.public_key()

    # 转换为字节
    private_key_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PrivateFormat.Raw,
        encryption_algorithm=serialization.NoEncryption()
    )

    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw
    )

    return private_key_bytes, public_key_bytes, seed


def sign_validation_payload(private_key_bytes: bytes, event_ts: str, plain_token: str) -> str:
    """对验证载荷进行 Ed25519 签名"""
    # 构建消息
    msg = event_ts + plain_token
    msg_bytes = msg.encode('utf-8')

    # 从字节加载私钥
    private_key = ed25519.Ed25519PrivateKey.from_private_bytes(private_key_bytes)

    # 签名
    signature = private_key.sign(msg_bytes)

    # 转换为十六进制字符串
    signature_hex = binascii.hexlify(signature).decode('utf-8')

    return signature_hex
