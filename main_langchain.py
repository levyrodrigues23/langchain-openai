from langchain_openai import ChatOpenAI
import os # para que eu possa usar as variaveis de ambiente
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate # antes era langchain.prompts, agora é langchain_core.prompts

load_dotenv()

numero_de_dias = 7
numero_de_criancas = 2
atividade = "praia"

modelo_do_prompt = PromptTemplate.from_template(
    "Crie um roteiro de viagem de {dias} dias, para uma familia com {criancas} crianças, que gostam de {atividade}."
)

prompt = modelo_do_prompt.format(
    dias=numero_de_dias,
    criancas=numero_de_criancas,
    atividade=atividade
)

print(prompt)

llm = ChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    model_name="gpt-3.5-turbo",
    temperature=0.5
)

resposta = llm.invoke(prompt)
print(resposta.content)

