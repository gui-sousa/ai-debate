from langchain_openai import ChatOpenAI
from config import Config as var

# Instanciando os Modelos
model_a = ChatOpenAI(
    base_url = var.model_a.URL,
    api_key = var.model_a.API_KEY,   
    model = var.model_a.MODEL_NAME,
    temperature = var.model_a.TEMP,
    max_tokens = var.model_a.TOKENS,
    frequency_penalty = var.model_a.PENALTY,
    top_p = var.model_a.TOP_P
)

model_b = ChatOpenAI(
    base_url = var.model_b.URL,
    api_key = var.model_b.API_KEY,   
    model = var.model_b.MODEL_NAME,
    temperature = var.model_b.TEMP,
    max_tokens = var.model_b.TOKENS,
    frequency_penalty = var.model_b.PENALTY,
    top_p = var.model_b.TOP_P
)