from llm_client import HelloAgentsLLM
from Reflection.reflection_agent import ReflectionAgent

if __name__ == "__main__":
    llm_client = HelloAgentsLLM()   # 初始化参数照抄你跑通的react_main.py里那行，一字不改
    agent = ReflectionAgent(llm_client)
    agent.run("编写一个Python函数，找出1到n之间所有的素数 (prime numbers)。")