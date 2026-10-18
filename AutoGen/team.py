# team.py
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination

def build_team(product_manager, engineer, code_reviewer, user_proxy):
    return RoundRobinGroupChat(
        participants=[product_manager, engineer, code_reviewer, user_proxy],
        termination_condition=TextMentionTermination("TERMINATE"),
        max_turns=20,
    )