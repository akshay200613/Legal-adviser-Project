# AI Legal Adviser Backend

Production-ready FastAPI backend for an AI-powered legal advisory platform.

## Features
- **Scalable Structure**: Modular routers and services.
- **Security**: JWT Authentication & RBAC (Role-Based Access Control).
- **Performance**: Async architecture with Redis caching.
- **Reliability**: Structured logging and global exception handling.
- **AI Ready**: Streaming response support for LLM interactions.
- **DevOps**: Multi-stage Docker build and Docker Compose setup.

## Getting Started

### Local Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set up environment:
   ```bash
   cp .env.example .env # Update with your values
   ```
3. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

### Running with Docker
```bash
docker-compose up --build
```

## API Documentation
Once the app is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Folder Structure
- `app/api`: API route definitions.
- `app/core`: Core configurations (security, config, logging).
- `app/middleware`: Custom FastAPI middlewares.
- `app/models`: Data models.
- `app/schemas`: Pydantic validation schemas.
- `app/services`: Business logic and AI integrations.
