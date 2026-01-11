# chatbot_mentor mentorPlanilha

# 1 - Importação das configurações e classes necessárias
from modelo_config import (
    modelo,
    ChatPromptTemplate,
    StrOutputParser,
    InMemoryChatMessageHistory,
    RunnableWithMessageHistory
)
from etapa2 import chain

# 2 - Dicionário para armazenar o histórico
memoria_sessoes = {}

# 3 - Função para obter histórico por sessão
def obter_historico_por_sessao(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in memoria_sessoes:
        memoria_sessoes[session_id] = InMemoryChatMessageHistory()
    return memoria_sessoes[session_id]

# 5 - Cadeia com memória
cadeia_com_memoria = RunnableWithMessageHistory(
    chain,
    obter_historico_por_sessao,
    input_messages_key="query",
    history_messages_key="historico",
)

# 6 - Laço de repetição
if __name__ == "__main__":
    perguntas = [
        "Eu estou aprendendo sobre Excel. Qual função é mais eficaz para selecionar uma quantidade específica de colunas?",
        "Em quais situações faz sentido utilizar o PROCX em detrimento do PROCV?"
    ]
    
    session_id = "sessao_usuario_1"
    
    for pergunta in perguntas:
        print(f"--- Pergunta: {pergunta} ---")
        resposta = cadeia_com_memoria.invoke(
            {"query": pergunta},
            config={"configurable": {"session_id": session_id}}
        )
        print(f"Resposta: {resposta}")
        print("-" * 80)
