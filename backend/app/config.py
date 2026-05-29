from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    BACKEND_URL: str = "http://localhost:8000"
    FRONTEND_URL: str = "http://localhost:3000"
    DATABASE_URL: str = "postgresql://rag_user:rag_password@localhost:5432/rag_analytics"
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "qwen:7b"
    OLLAMA_TEMPERATURE: float = 0.7
    MAX_UPLOAD_SIZE: int = 104857600
    UPLOAD_DIR: str = "/tmp/uploads"
    ALLOWED_EXTENSIONS: List[str] = ["csv", "xlsx", "xls", "pdf"]
    VECTOR_DB_PATH: str = "/tmp/faiss_db"
    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
    LOG_LEVEL: str = "INFO"
    LOG_DIR: str = "/tmp/logs"
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:5173"]
    CORS_CREDENTIALS: bool = True
    CORS_METHODS: List[str] = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
    CORS_HEADERS: List[str] = ["*"]
    REPORT_OUTPUT_DIR: str = "/tmp/reports"

    class Config:
        env_file = ".env"

settings = Settings()
