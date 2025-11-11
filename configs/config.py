import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()  # 加载 .env 文件


class Settings(BaseSettings):
    """应用配置"""

    # Bot 配置
    BOT_APPID: str = os.getenv("BOT_APPID", "")
    BOT_SECRET: str = os.getenv("BOT_SECRET", "")
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
    SIGN_HOST: str = os.getenv("SIGN_HOST", "")
    class Config:
        env_file = ".env"


# 创建全局配置实例
settings = Settings()