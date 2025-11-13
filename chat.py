from langchain_openai import ChatOpenAI
import os # para que eu possa usar as variaveis de ambiente
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate # antes era langchain.prompts, agora é langchain_core.prompts

load_dotenv()
def menu():
    while True:
        input_usuario = input("faça uma pergunta:")
                
        modelo_do_prompt = PromptTemplate.from_template(
            "voce é um assistente safada e que ama falar sobre sexo. Responda a seguinte pergunta: {input_usuario}."
        )

        prompt = modelo_do_prompt.format(
            input_usuario=input_usuario
        )


        print(prompt)

        llm = ChatOpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            model_name="gpt-3.5-turbo",
            temperature=0.5
        )

        resposta = llm.invoke(prompt)
        print(resposta.content)

# Chamando a função menu para iniciar o chat
menu()

