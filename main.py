from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START
from nodes import run_model_a, run_model_b
from edges import moderator
from config import Config as var
from config import debate_state

# Criando StateGraph
box = StateGraph(debate_state)

# Criando os Nodes
box.add_node("Debater_A", run_model_a)
box.add_node("Debater_B", run_model_b)

# Criando as Arestas
box.add_edge(START, "Debater_A")
box.add_edge("Debater_A", "Debater_B")
box.add_conditional_edges("Debater_B", moderator)

# Instanciando o Grafo
app = box.compile()

if __name__ == "__main__":
    init_message = HumanMessage(
        content = f"O tema do debate é: {var.debate.TOPIC}! Voce é livre para falar e se expressar como quiser"
    )
    print(f"▶️ Iniciando o debate...\n🧐 Pergunta Inicial:{init_message.content}\n" + "-"*50)

    # Define o numero maximo de interação entre os nodes, caso no numero de ROUNDS seja ultrapassado
    config = {"recursion_limit": 15}

    init_state = {
        "messages": [init_message],
        "turn_count": 0
    }

    for event in app.stream(init_state, config=config):
        for no, data in event.items():
            last_message = data["messages"][-1]
            print(f"\n[🎙️{no}]:{last_message.content}")
            print("🔸" * 60)
    print(f"\n{'-'*60}\n🙅🏾‍♂️🙅🏾‍♂️🙅🏾‍♂️\nDEBATE ENCERRADO!")