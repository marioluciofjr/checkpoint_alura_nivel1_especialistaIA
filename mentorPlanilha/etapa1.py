# chatbot_mentor mentorPlanilha

# 1 - Importação das configurações e classes necessárias
from modelo_config import modelo

# 2 - Lista com duas perguntas sequenciais
perguntas = [
    "Eu estou aprendendo sobre Excel. Qual função é mais eficaz para selecionar uma quantidade específica de colunas?",
    "Em quais situações faz sentido utilizar o PROCX em detrimento do PROCV?"
]

# 3 - Laço de repetição para enviar perguntas e imprimir respostas
for pergunta in perguntas:
    resposta = modelo.invoke(pergunta)
    print(f"Pergunta: {pergunta}")
    print(f"Resposta: {resposta.content}")
    print("-" * 80)