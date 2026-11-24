
from pydantic import BaseModel, Field


# 客户端请求的数据格式
class AskRequest(BaseModel):

    msg: str = Field(
        min_length=1,
        max_length=100,
        description="消息内容"
    )

    user_id: str = Field(
        min_length=1,
        description="用户ID"
    )


# 服务器返回的数据格式
class ResponseRequest(BaseModel):

    answer: str

    success: bool
