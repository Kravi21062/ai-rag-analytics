from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, EmailStr, Field

class UserRegister(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    full_name: str = Field(min_length=2)

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    full_name: str
    created_at: datetime
    class Config:
        from_attributes = True

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int

class DatasetMetadata(BaseModel):
    id: int
    name: str
    filename: str
    file_type: str
    size: int
    rows: int
    columns: int
    data_quality_score: float
    created_at: datetime
    class Config:
        from_attributes = True

class AnalyticsQuery(BaseModel):
    dataset_id: int
    query: str
    model: Optional[str] = None

class ChatRequest(BaseModel):
    dataset_id: int
    message: str
    model: Optional[str] = None

class ChatResponse(BaseModel):
    message: str
    charts: List[Dict[str, Any]] = []
    insights: List[str] = []

class ForecastRequest(BaseModel):
    dataset_id: int
    column: str
    periods: int = 30
    method: str = "prophet"

class AnomalyDetectionRequest(BaseModel):
    dataset_id: int
    column: str
    method: str = "isolation_forest"
    contamination: float = 0.1
