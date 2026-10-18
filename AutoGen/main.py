# main.py
import asyncio
from autogen_agentchat.ui import Console
from llm_client import create_openai_model_client   # 复用根目录的
from agents import (create_product_manager, create_engineer,
                    create_code_reviewer, create_user_proxy)
from team import build_team

async def main():
    model_client = create_openai_model_client()
    team = build_team(
        create_product_manager(model_client),
        create_engineer(model_client),
        create_code_reviewer(model_client),
        create_user_proxy(),          # 注意：它不接收 model_client
    )
    task = "请团队成员互相打个招呼，每人一句话，然后结束。"
    await Console(team.run_stream(task=task))

if __name__ == "__main__":
    asyncio.run(main())