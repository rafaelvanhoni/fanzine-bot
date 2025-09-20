# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v0.1.0] - 2025-09-13
### Added
- Initial project structure
- `README.md` (English) and `README.pt-BR.md` (Portuguese)
- `CHANGELOG.md` following the *Keep a Changelog* format
- `requirements.txt` with minimal dependencies
- `.env.example` for sensitive variables
- MIT license configuration
- Directory structure with `app/` and `tests/`

## [v0.2.0] - 2025-09-19
### Added
- Initial integration with the Discogs API via `DiscogsService`, including error handling for HTTP codes 401, 404, 429, and 5xx.
- `Artist` class with support for `from_dict`, `__str__`, and `__repr__`.
- Custom `DiscogsError` exception to handle Discogs API communication errors.
- `main.py` demonstrating the artist search flow (e.g., query for "Ramones").
- Initial test structure:  
  - `test_artist.py` validating textual representation.  
  - `test_discogs_service.py` with stubs for error scenarios.