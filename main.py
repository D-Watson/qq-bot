from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from data.WebhookBody import PayLoad
from services import message_service


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_token_to_response_headers(request: Request, call_next):
    # 处理请求
    response = await call_next(request)

    # 生成或获取 token
    token = message_service.get_access_token()

    # 添加自定义响应头
    response.headers["Authorization"] = "QQBot "+token
    return response


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/callback")
async def sign(payload: PayLoad):
    res = message_service.deal_callback(payload)
    return res

