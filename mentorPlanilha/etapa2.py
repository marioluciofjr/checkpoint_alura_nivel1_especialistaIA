# chatbot_mentor mentorPlanilha

# 1 - Importação das configurações e classes necessárias
from modelo_config import modelo, ChatPromptTemplate, StrOutputParser

# 2 - Criação do Template de Prompt
# Define o comportamento do sistema, o placeholder para histórico e a entrada do usuário
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "Você é o 'mentorPlanilha', um assistente especializado em ajudar pessoas a entenderem mais sobre o Excel. Seja amigável e didático."),
    ("placeholder", "{historico}"),
    ("human", "{query}"),
])

# 3 - Criação da Cadeia (Chain)
# Conecta o prompt, o modelo e o parser de saída usando LCEL
chain = prompt_template | modelo | StrOutputParser()

# 4 - Execução local para teste
if __name__ == "__main__":
    resposta = chain.invoke(
        {
            "query" : "Qual função é mais eficaz para classificar uma lista de valores?"
        }
    )
    print(resposta)

