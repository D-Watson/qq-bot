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

    # 服务器配置
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))

    # 功能开关
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    ENABLE_WEBHOOK: bool = os.getenv("ENABLE_WEBHOOK", "true").lower() == "true"

    # 日志配置
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE: str = os.getenv("LOG_FILE", "bot.log")

    class Config:
        env_file = ".env"


# 创建全局配置实例
settings = Settings()