import os
from dotenv import load_dotenv
from pathlib import Path
from autogen_ext.models.openai import OpenAIChatCompletionClient

load_dotenv(Path(__file__).parent.parent / ".env")

def create_openai_model_client():
    """创建并配置模型客户端（百炼/通义千问）"""
    return OpenAIChatCompletionClient(
        model=os.getenv("LLM_MODEL_ID"),
        api_key=os.getenv("LLM_API_KEY"),
        base_url=os.getenv("LLM_BASE_URL"),
        model_info={
            "function_calling": True,
            "max_tokens": 8192,
            "context_length": 131072,
            "vision": False,
            "json_output": True,
            "family": "qwen",
            "structured_output": True,
        },
    )