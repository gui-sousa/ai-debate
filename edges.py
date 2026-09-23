from langgraph.graph import END
from config import Config as var

# Função para definir o final do Debate
def moderator(state):
    if state["turn_count"] >= var.debate.ROUNDS:
        return END
    return "Debater_A"