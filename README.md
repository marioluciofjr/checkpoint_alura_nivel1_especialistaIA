# mentorPlanilha

Projeto para cumprir o checkpoint do Nível 1 da Carreira "Especialista em IA", da Alura.

[![Made with Python](https://img.shields.io/badge/Python->=3.10-blue?logo=python&logoColor=white)](https://python.org "Go to Python homepage")
![license - MIT](https://img.shields.io/badge/license-MIT-green)
![site - prazocerto.me](https://img.shields.io/badge/site-prazocerto.me-230023)
![linkedin - @marioluciofjr](https://img.shields.io/badge/linkedin-marioluciofjr-blue)

## Índice

* [Introdução](#introdução)
* [Estrutura do projeto](#estrutura-do-projeto)
* [Tecnologias utilizadas](#tecnologias-utilizadas)
* [Requisitos](#requisitos)
* [Links úteis](#links-úteis)
* [Contribuições](#contribuições)
* [Licença](#licença)
* [Contato](#contato)

## Introdução
O mentorPlanilha é um chatbot inteligente projetado para auxiliar usuários a dominarem o Excel. Utilizando a poderosa e gratuita API da Groq, este projeto oferece orientações precisas sobre fórmulas e funções. Ele nasceu como uma adaptação de uma prova prática da Alura, transformando-se em uma ferramenta prática que responde a perguntas e mantém o contexto da conversa. O objetivo é oferecer uma experiência de mentoria contínua, personalizada e didática para todos que buscam eficiência e clareza na análise de dados com planilhas eletrônicas.

## Estrutura do projeto
Este projeto é organizado em etapas incrementais que demonstram a construção de um chatbot com LangChain:

*   **`modelo_config.py`**: Arquivo central de configuração. Responsável por carregar as variáveis de ambiente (como a API Key) e inicializar o modelo de linguagem e os componentes compartilhados do LangChain.
*   **`etapa1.py`**: A primeira versão do bot. Implementa um laço simples que envia perguntas sequenciais para a IA, sem manter contexto ou usar templates complexos.
*   **`etapa2.py`**: Evolução para o uso de `PromptTemplates` e cadeias LCEL (LangChain Expression Language). Aqui estruturamos melhor a entrada e a saída do modelo.
*   **`etapa3.py`**: A versão final com memória. Implementa o histórico de sessões, permitindo que o bot "lembre" do que foi conversado anteriormente, simulando uma interação humana real.

### Contexto e Adaptação

Este projeto é uma adaptação prática do desafio proposto no checkpoint do nível 1 da carreira "Especialista em IA" da Alura. Originalmente, o desafio sugeria a criação do **"GeoAI Mentor"**, com a seguinte premissa:

> "Muitos estudantes e profissionais da área de Geociências (como Geofísica e Geologia) possuem uma base sólida em matemática e física, mas encontram dificuldades para migrar para a área de Ciência de Dados e Inteligência Artificial. Eles frequentemente têm dúvidas sobre quais habilidades transferir, que linguagens de programação aprender e como aplicar seus conhecimentos de domínio em projetos de dados.
>
> Seu desafio é desenvolver o 'GeoAI Mentor', um chatbot assistente especializado. Este chatbot atuará como um mentor de carreira, respondendo a perguntas de geocientistas que desejam fazer essa transição. O diferencial do 'GeoAI Mentor' será sua capacidade de manter o contexto da conversa, lembrando das perguntas e respostas anteriores para fornecer um aconselhamento coeso e personalizado, como um verdadeiro mentor faria."

Para este projeto, optei por adaptar o tema para o **mentorPlanilha**, focando em Excel, mas mantendo a lógica de progressão e a arquitetura de software proposta.

### Diferencial Técnico: Groq API
Uma mudança fundamental nesta implementação foi a substituição da API da OpenAI pela **API da Groq**. A Groq oferece inferência extremamente rápida e um plano gratuito generoso para desenvolvedores.

Para rodar este projeto, você precisará de uma chave de API gratuita:
1.  Acesse a [documentação da Groq Console](https://console.groq.com/docs/overview).
2.  Crie sua conta e gere uma `API Key`.
3.  Adicione-a ao seu arquivo `.env`.

> [!TIP]
> Veja a execução do projeto no gif
> <img width="1910" height="1004" alt="image" src="https://github.com/user-attachments/assets/acf47280-1399-4bd0-9843-f20c20d1d919" />


> [!IMPORTANT]
> Se quiser conversar sobre esse projeto, basta acessar a versão [`TalkToGitHub`](https://talktogithub.com/marioluciofjr/checkpoint_alura_nivel1_especialistaIA) <br>
> Want to better understand this repository, but you don't speak Portuguese? Check out this complete tutorial: [`Codebase - prompt_personagem_ia`](https://code2tutorial.com/tutorial/9ebd63ce-6ac7-4b2e-883f-92e74953efde/index.md)

## Tecnologias utilizadas

<div>
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/76e7aca0-5321-4238-9742-164c20af5b4a" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://camo.githubusercontent.com/13caad70455ed743a53c3624ce9e033554f2aabc28a46c14f43e05214f963a92/68747470733a2f2f692e6e616d752e77696b692f692f6b415278316e5039474861546b74785f347954493448584c4f6a6d64334a5a614b4a6b48545867453262763455415457586b566c766f45366b74464f344d464936794d6356353078367a2d7069734f4544424f554f512e77656270" />&nbsp;&nbsp;&nbsp
 </div><br>

* Python;
* Antigravity.

## Requisitos

Antes de começar, certifique-se de ter instalado:
*   [Python 3.10](https://www.python.org/downloads/) ou superior.
*   [UV](https://github.com/astral-sh/uv) (Recomendado) ou PIP.

## Links úteis

* [Como instalar o VSCode](https://code.visualstudio.com/download)- Link direto para download
* [Documentação oficial do pacote uv](https://docs.astral.sh/uv/) - Você saberá todos os detalhes sobre o `uv` e como ele é importante no Python
* [venv — Criação de ambientes virtuais](https://docs.python.org/pt-br/3/library/venv.html) - Explicação completa de como funcionam os venvs
* [Conjunto de ícones de modelos de IA/LLM](https://lobehub.com/pt-BR/icons) - site muito bom para conseguir ícones do ecossistema de IA
* [Devicon](https://devicon.dev/) - site bem completo também com ícones gerais sobre tecnologia
* [Smolagents](https://github.com/huggingface/smolagents) - documenttação oficial da biblioteca smolagents
* [Como baixar o Antigravity](https://antigravity.google/download) - Página oficial de download da IDE do Google DeepMind
* [Documentação LangChain](https://docs.langchain.com) - Página oficial do LangChain, framework importante para vários projetos em Python com IA generativa
* [APIs Groq](https://console.groq.com/keys) - Link para gerar uma api_key no Groq
* [Carreira 'Especialista em IA'](https://www.alura.com.br/carreiras/especialista-em-ia) - Página oficial da Alura

## Contribuições

Contribuições são bem-vindas! Se você tem ideias para melhorar este projeto, sinta-se à vontade para fazer um fork do repositório.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](https://github.com/marioluciofjr/checkpoint_alura_nivel1_especialistaIA/blob/main/LICENSE) para detalhes.

## Contato
    
Mário Lúcio - Prazo Certo®
<div>  	
  <a href="https://www.linkedin.com/in/marioluciofjr" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> 
  <a href = "mailto:marioluciofjr@gmail.com" target="_blank"><img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white"></a>
  <a href="https://prazocerto.me/contato" target="_blank"><img src="https://img.shields.io/badge/prazocerto.me/contato-230023?style=for-the-badge&logo=wordpress&logoColor=white"></a>
</div> 
