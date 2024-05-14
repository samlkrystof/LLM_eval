import os
from typing import Optional

from langchain_community.chat_models import ChatOpenAI


class ChatOpenRouter(ChatOpenAI):
    def __init__(self,
                 model_name: str,
                 openai_key: Optional[str],
                 openai_api_base: str = "https://openrouter.ai/api/v1",
                 **kwargs):
        openai_key = openai_key or os.getenv("OPENAI_KEY")
        super().__init__(model_name, openai_key, openai_api_base, **kwargs)
