from langchain_openai import ChatOpenAI
import os # para que eu possa usar as variaveis de ambiente
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate # antes era langchain.prompts, agora é langchain_core.prompts
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory


load_dotenv()

numero_de_dias = 7
numero_de_criancas = 2
atividade = "praia"



llm = ChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    model_name="gpt-3.5-turbo",
    temperature=0.5
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente útil."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

# é bem interessante o contexto que a llm está funcionando, so que essa ideia de armazenar tudo em uma string pode ser limitada, justamente porque a mensagem vai crescer tanto que a ia não vai acabar lembrando das mensagens anteriores praticamete ou seja por si so isso vai ficar um pouco fora do comum como realmente deveria ser
store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]
        
chain = prompt | llm 

chain_with_memory = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)
mensagens = [
    "Meu nome é José Luis",
    "Qual é o meu nome?",
    "Eu gosto de Itapajé",
    "Do que eu gosto?"
]

# agora vamos usar o chatprompttemplate e o runnablewithmessagehistory
# para que a llm possa lembrar de todas as mensagens
session_id = "sessao_1"

for msg in mensagens:
    resposta = chain_with_memory.invoke(
        {"input": msg},
        config={"configurable": {"session_id": session_id}}
    )
    print(f"Você: {msg}")
    print(f"AI: {resposta.content}\n")

