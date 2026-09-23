from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages

# Dicionário onde os arqgumentos do debate são registrados
class debate_state(TypedDict):
    messages: Annotated[list, add_messages]
    turn_count: int

# DEBATE RULES

class Config: 
    class debate :
        TOPIC = "Quem vencerá a Copa de 2026?"
        ROUNDS = 6

    class model_a : 
        URL = ""
        API_KEY = ""
        MODEL_NAME = ""
        TEMP = "0.9"
        TOKENS = 1500
        PENALTY = 0.7
        TOP_P = 0.9


    class model_b :
        URL = ""
        API_KEY = ""
        MODEL_NAME = ""
        TEMP = "0.9"
        TOKENS = 800
        PENALTY = 0.7
        TOP_P = 0.9
