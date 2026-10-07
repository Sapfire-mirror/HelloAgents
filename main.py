from llm_client import HelloAgentsLLM
from executor import ToolExecutor
from search import search
from react_agent import ReActAgent

llm = HelloAgentsLLM()

executor = ToolExecutor()
search_description = "一个网页搜索引擎。当你需要回答关于时事、事实以及在你的知识库中找不到的信息时，应使用此工具。"
executor.registerTool("Search", search_description, search)

agent = ReActAgent(llm_client=llm, tool_executor=executor)
answer = agent.run("英伟达最新的GPU型号是什么？")
print(f"\n最终答案: {answer}")