
import logging

from fastapi import APIRouter, HTTPException

from schemas.chat import AskRequest, ResponseRequest
from services.llm import LLMService


logger = logging.getLogger(__name__)

# 创建路由
router = APIRouter()

# 创建 LLM 服务对象
llm_service = LLMService()


@router.post("/chat", response_model=ResponseRequest)
async def chat(request: AskRequest):

    logger.info(
        "收到聊天请求，user_id=%s",
        request.user_id
    )

    try:
        # 调用 LLM Service
        answer = await llm_service.generate(request.msg)

        # 返回响应
        return ResponseRequest(
            answer=answer,
            success=True
        )

    except Exception:
        logger.exception("聊天请求处理失败")

        raise HTTPException(
            status_code=500,
            detail="服务器内部错误"
        )
