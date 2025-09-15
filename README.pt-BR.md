# fanzine-bot 🎸🤖

## Sobre o projeto
O **fanzine-bot** é um projeto educativo em Python que une música e tecnologia.  
A proposta é explorar a API do Discogs e evoluir com recursos de Inteligência Artificial para criar um catálogo pessoal, gerar recomendações automáticas, construir playlists e experimentar visualizações criativas no estilo fanzine.

## Objetivos técnicos
- Aplicar boas práticas modernas de desenvolvimento: OO, SOLID, Clean Architecture, DDD, TDD.
- Explorar recursos de IA aplicados a dados musicais:
  - **Embeddings** e similaridade (sentence-transformers).
  - **Busca vetorial** (FAISS ou ChromaDB) para RAG.
  - **LLMs** (Ollama/OpenAI/Groq) para resumos e respostas contextuais.
  - **Sistemas de recomendação** baseados em conteúdo.
- Construir uma interface web simples com **Streamlit**.
- Integrar com **YouTube Music API (ytmusicapi)** para geração automática de playlists.
- Persistência em **JSON/SQLite** para cache, favoritos e playlists.

## Roadmap (alto nível)
1. Catálogo pessoal com busca no Discogs e favoritos persistentes  
2. Conexões entre artistas/bandas com visualização em grafo  
3. Chatbot underground com RAG sobre dados musicais  
4. Curador de playlists no YouTube Music com descrições automáticas  
5. Visualizações e experimentos no estilo fanzine  

## Stack inicial
- **Linguagem:** Python 3.x  
- **UI:** Streamlit  
- **APIs:** Discogs API, YouTube Music API  
- **IA/NLP:** sentence-transformers, FAISS/ChromaDB, LLMs  
- **Qualidade:** pytest, black, ruff, isort, loguru  
- **Persistência:** JSON/SQLite  

## Licença
MIT — veja o arquivo [LICENSE](LICENSE) para mais detalhes.