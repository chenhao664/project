
from fastapi import FastAPI

from core.config import setup_logging
from routes.chat import router as chat_router


# 初始化日志
setup_logging()

# 创建 FastAPI 应用
app = FastAPI(
    title="LLM Chat API",
    description="基于 FastAPI 的大模型聊天接口",
    version="1.0.0"
)

# 注册聊天路由
app.include_router(chat_router)


@app.get("/")
async def root():
    return {
        "message": "LLM Chat API is running",
        "success": True
    }
