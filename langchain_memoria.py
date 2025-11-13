from langchain_openai import ChatOpenAI
import os # para que eu possa usar as variaveis de ambiente
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate # antes era langchain.prompts, agora é langchain_core.prompts
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

load_dotenv()

numero_de_dias = 7
numero_de_criancas = 2
atividade = "praia"

modelo_do_prompt = PromptTemplate.from_template(
    "Crie um roteiro de viagem de {dias} dias, para uma familia com {criancas} crianças, que gostam de {atividade}."
)


llm = ChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    model_name="gpt-3.5-turbo",
    temperature=0.5
)

mensagens = [
    "armazene que meu nome é jose luis e que eu gosto de itapaje.",
    "qual o meu nome?",
    "quero saber sobre a cultura de itapaje.",
    "quero saber sobre a gastronomia de itapaje.",
    "quero saber sobre as mulheres de itapaje."
]

# é bem interessante o contexto que a llm está funcionando, so que essa ideia de armazenar tudo em uma string pode ser limitada, justamente porque a mensagem vai crescer tanto que a ia não vai acabar lembrando das mensagens anteriores praticamete ou seja por si so isso vai ficar um pouco fora do comum como realmente deveria ser

longa_conversa = ""
for mensagem in mensagens:
    longa_conversa += f"Usuário: {mensagem}\n"
    longa_conversa += f"AI: "

    modelo = PromptTemplate(template=longa_conversa, input_variables=[""])
    cadeia = modelo | llm | StrOutputParser()
    resposta = cadeia.invoke(input={})
    #print(resposta)
    
    longa_conversa += resposta + "\n"   
    print(longa_conversa)