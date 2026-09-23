from langchain_core.messages import HumanMessage, AIMessage
from config import debate_state
from models import model_a, model_b
from prompts import system_prompt_a, system_prompt_b

# Converte IAMessage in HumanMessage
def format_history(history, debater):
    formatted_context = []
    
    for message in history:
        if isinstance(message, AIMessage) and message.name == debater:
            nova_msg = HumanMessage(content=message.content, name=debater)
        else:
            nova_msg = message
            
        if formatted_context and isinstance(nova_msg, type(formatted_context[-1])):
            msg_anterior = formatted_context.pop()
            texto_junto = f"{msg_anterior.content}\n\n---\n\n{nova_msg.content}"
            msg_combinada = type(nova_msg)(content=texto_junto)
            formatted_context.append(msg_combinada)
        else:
            formatted_context.append(nova_msg)

    return formatted_context

# Debaters functions
def run_model_a(state: debate_state):
    history = state["messages"]
    ai_history = format_history(history, debater="Debater_B")
    context = [system_prompt_a] + ai_history
    try:
        response = model_a.invoke(context)
        response.name = "Debater_A"
    except Exception as e:
        response = AIMessage(content=f"[Erro na conexão com o modelo (A):\n{str(e)}]")
        response.name = "Debater_A"
    return {
        "messages": [response]  
    }

def run_model_b(state: debate_state):
    history = state["messages"]
    ai_history = format_history(history, debater="Debater_B")
    context = [system_prompt_b] + ai_history
    try:
        response = model_b.invoke(context)
        response.name = "Debater_B"
    except Exception as e:
        response = AIMessage(content=f"[Erro na conexão com o modelo (B):\n{str(e)}]")
        response.name = "Debater_B"

    return {
        "messages": [response],
        "turn_count": state["turn_count"] + 1    
    }
