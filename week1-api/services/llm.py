
import logging

logger = logging.getLogger(__name__)


class LLMService:

    async def generate(self, msg: str) -> str:
        """
        接收用户消息，生成模型回答
        """

        try:
            logger.info("开始调用 LLM")

            # 模拟 LLM 返回
            answer = f"这是模型对你的回答：{msg}"

            logger.info("LLM 调用成功")

            return answer

        except Exception:
            logger.exception("LLM 调用失败")
            raise
