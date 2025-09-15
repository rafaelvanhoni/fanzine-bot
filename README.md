# fanzine-bot 🎸🤖

## About the project
**fanzine-bot** is an educational Python project that blends music and technology.  
The goal is to explore the Discogs API and evolve with Artificial Intelligence features to build a personal catalog, generate automatic recommendations, create playlists, and experiment with creative “fanzine-style” visualizations.

## Technical objectives
- Apply modern software development practices: OOP, SOLID, Clean Architecture, DDD, TDD.
- Explore AI techniques applied to music data:
  - **Embeddings** and similarity (sentence-transformers).
  - **Vector search** (FAISS or ChromaDB) for RAG.
  - **LLMs** (Ollama/OpenAI/Groq) for summaries and contextual answers.
  - **Content-based recommendation systems**.
- Build a simple web interface with **Streamlit**.
- Integrate with **YouTube Music API (ytmusicapi)** for automatic playlist generation.
- Use **JSON/SQLite** for caching, favorites, and playlists.

## Roadmap (high-level)
1. Personal catalog with Discogs search and persistent favorites  
2. Artist/band connections with interactive graph visualization  
3. Underground chatbot with RAG over music data  
4. Playlist curator on YouTube Music with AI-generated descriptions  
5. Visualizations and experiments inspired by DIY fanzines  

## Tech stack
- **Language:** Python 3.x  
- **UI:** Streamlit  
- **APIs:** Discogs API, YouTube Music API  
- **AI/NLP:** sentence-transformers, FAISS/ChromaDB, LLMs  
- **Quality:** pytest, black, ruff, isort, loguru  
- **Persistence:** JSON/SQLite  

## License
MIT — see the [LICENSE](LICENSE) file for details.

---

> This README is also available in [Portuguese](README.pt-BR.md).