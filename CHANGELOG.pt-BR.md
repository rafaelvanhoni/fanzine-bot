# Changelog
Todas as mudanças notáveis deste projeto serão documentadas aqui.

O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/)
e este projeto adere ao [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v0.1.0] - 2025-09-13
### Added
- Estrutura inicial do projeto
- Arquivo `README.md` (inglês) e `README.pt-BR.md` (português)
- Arquivo `CHANGELOG.md` seguindo o padrão *Keep a Changelog*
- Arquivo `requirements.txt` com dependências mínimas
- Arquivo `.env.example` para variáveis sensíveis
- Configuração de licença MIT
- Estrutura de pastas `app/` e `tests/`

## [v0.2.0] - 2025-09-19
### Added
- Integração inicial com a API do Discogs via `DiscogsService`, incluindo tratamento de erros HTTP (401, 404, 429 e 5xx).
- Classe `Artist` com suporte a `from_dict`, `__str__` e `__repr__`.
- Exceção personalizada `DiscogsError` para isolar erros de comunicação com a API.
- `main.py` demonstrando o fluxo de consulta de artistas (ex.: busca por "Ramones").
- Estrutura inicial de testes:  
  - `test_artist.py` validando representação textual.  
  - `test_discogs_service.py` com stubs para cenários de erro.