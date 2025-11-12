from langchain_openai import ChatOpenAI
import os 
from dotenv import load_dotenv

load_dotenv()

numero_de_dias = 7
numero_de_criancas = 2
atividade = "praia"

prompt = f"Crie um roteiro de viagem de {numero_de_dias} dias, para uma familia com {numero_de_criancas} crianças, que gostam de {atividade}."

llm = ChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    model_name="gpt-3.5-turbo",
    temperature=0.5
)

resposta = llm.invoke(prompt)
print(resposta.content)

