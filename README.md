# AI-Powered RAG Analytics Assistant

A production-ready, next-generation AI analytics platform with local LLM support, real-time data analysis, and intelligent insights generation.

## 🚀 Features

### Core Analytics
- 📊 Multi-format data upload (CSV, Excel, PDF)
- 🤖 Natural language analytics queries
- 📈 Auto-generated visualizations
- 🔮 Trend forecasting (Prophet, ARIMA, XGBoost)
- 🚨 Anomaly detection
- 💡 AI-powered business insights
- 🔍 Semantic search with RAG
- 💬 Conversational memory
- 📝 SQL query generation
- 📊 Dashboard auto-generation

### AI/ML Capabilities
- Multi-agent AI workflows (Data Analyst, Visualizer, Forecaster, Report Writer)
- Local LLM support (Qwen3, Llama3 via Ollama)
- Vector embeddings with FAISS
- Document chunking & retrieval
- Semantic understanding

### User Features
- 🎨 Modern, responsive dashboard
- 🔐 JWT authentication
- 📁 Project management
- 💾 Export (CSV, Excel, PDF, PNG)
- 🌙 Dark/Light mode
- 📱 Mobile-friendly UI
- 🎤 Voice query support (Whisper)
- 📊 Real-time charts

### DevOps
- 🐳 Docker & Docker Compose
- 📦 PostgreSQL database
- ⚡ Async FastAPI backend
- 🔄 Scalable architecture
- 📊 Logging & monitoring

---

## 🛠️ Tech Stack

### Frontend
- **React 18** with TypeScript
- **TailwindCSS** for styling
- **shadcn/ui** for components
- **Framer Motion** for animations
- **Recharts** for visualizations
- **Axios** for API calls

### Backend
- **FastAPI** (Python 3.12+)
- **PostgreSQL** for data storage
- **LangChain** for LLM orchestration
- **FAISS** for vector search
- **Sentence-Transformers** for embeddings
- **Prophet** for time-series forecasting
- **XGBoost** for ML predictions
- **Scikit-learn** for analytics
- **Pandas & NumPy** for data processing

### AI/LLM
- **Ollama** for local LLM execution
- **Qwen3** / **Llama3** models
- **LangChain** for agent workflows
- **Sentence-Transformers** for semantic embeddings

### Infrastructure
- **Docker & Docker Compose**
- **JWT Authentication**
- **CORS** for cross-origin requests

---

## 📋 Prerequisites

### Required Software
1. **Docker & Docker Compose** - [Install](https://docs.docker.com/get-docker/)
2. **Ollama** - [Install](https://ollama.ai)
3. **Node.js 18+** - [Install](https://nodejs.org/)
4. **Python 3.12+** - [Install](https://python.org/)

### For Local Development (Optional)
- PostgreSQL 15+
- npm or yarn
- Git

---

## 🚀 Quick Start

### Option 1: Docker Compose (Recommended)

```bash
# Clone repository
git clone https://github.com/Kravi21062/ai-rag-analytics.git
cd ai-rag-analytics

# Pull Ollama models
ollama pull qwen:7b
ollama pull llama2:7b

# Start services
docker-compose up -d

# Wait for services to be ready (2-3 minutes)
sleep 10

# Initialize database
docker-compose exec backend python scripts/init_db.py

# Access dashboard
open http://localhost:3000
```

### Option 2: Local Development

#### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Start FastAPI server
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Frontend Setup
```bash
cd frontend
npm install
npm run dev
# Access at http://localhost:5173
```

---

## 📁 Project Structure

```
ai-rag-analytics/
├── backend/                    # FastAPI application
│   ├── app/
│   │   ├── main.py            # FastAPI app entry
│   │   ├── auth/              # Authentication logic
│   │   ├── api/               # API endpoints
│   │   ├── services/          # Business logic
│   │   ├── ai/                # AI/ML pipelines
│   │   ├── models/            # Pydantic models
│   │   └── database/          # Database setup
│   ├── scripts/
│   │   ├── init_db.py         # Database initialization
│   │   └── seed_data.py       # Sample data
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env.example
│
├── frontend/                   # React application
│   ├── src/
│   │   ├── components/        # React components
│   │   ├── pages/             # Page components
│   │   ├── services/          # API clients
│   │   ├── hooks/             # Custom hooks
│   │   ├── types/             # TypeScript types
│   │   ├── utils/             # Utility functions
│   │   ├── styles/            # Tailwind config
│   │   └── App.tsx
│   ├── public/                # Static assets
│   ├── package.json
│   ├── Dockerfile
│   ├── vite.config.ts
│   └── tailwind.config.js
│
├── docker-compose.yml         # Docker services
├── .env.example               # Environment template
└── docs/                       # Documentation
```

---

## 🔑 Key Features Explained

### 1. RAG Pipeline
- Upload documents (CSV, Excel, PDF)
- Automatic chunking and embedding
- FAISS-powered semantic search
- Context-aware responses

### 2. Multi-Agent System
- **Data Analyst Agent**: Analyzes datasets, generates insights
- **Visualization Agent**: Creates appropriate charts
- **Forecasting Agent**: Generates predictions
- **Report Writer Agent**: Creates comprehensive reports
- **SQL Agent**: Converts natural language to SQL

### 3. Anomaly Detection
- Isolation Forest for outlier detection
- DBSCAN for cluster anomalies
- Configurable sensitivity
- Real-time alerts

### 4. Forecasting
- Prophet for time-series
- ARIMA models
- XGBoost for complex patterns
- Confidence intervals
- Visual forecasts

### 5. Chat Memory
- Conversational context
- Session persistence
- Query history
- Response caching

---

## 🔐 Authentication

### User Registration
```bash
POST /api/auth/register
{
  "email": "user@example.com",
  "password": "secure_password",
  "full_name": "John Doe"
}
```

### Login
```bash
POST /api/auth/login
{
  "email": "user@example.com",
  "password": "secure_password"
}
```

### Protected Routes
All API endpoints (except auth) require JWT token:
```bash
Authorization: Bearer {token}
```

---

## 📊 API Endpoints

### Datasets
- `POST /api/datasets/upload` - Upload file
- `GET /api/datasets` - List datasets
- `GET /api/datasets/{id}` - Get dataset details
- `DELETE /api/datasets/{id}` - Delete dataset
- `GET /api/datasets/{id}/preview` - Preview data

### Analytics
- `POST /api/analytics/analyze` - Analyze with NLP
- `POST /api/analytics/insights` - Generate insights
- `POST /api/analytics/forecast` - Generate forecast
- `POST /api/analytics/anomalies` - Detect anomalies
- `POST /api/analytics/correlations` - Get correlations

### Chat
- `POST /api/chat/message` - Send query
- `GET /api/chat/history` - Get chat history
- `DELETE /api/chat/history` - Clear history

### SQL
- `POST /api/sql/generate` - Convert NLP to SQL
- `POST /api/sql/execute` - Execute SQL query

### Reports
- `POST /api/reports/generate` - Create PDF report
- `GET /api/reports/{id}` - Download report

---

## 🎨 UI Components

### Dashboard
- KPI cards with metrics
- Real-time charts
- Dataset browser
- Upload drag-drop zone

### Chat Interface
- Message history
- Real-time responses
- Chart rendering
- Code snippets

### Analytics Views
- Forecasting dashboard
- Anomaly detection panel
- Correlation matrix
- Feature importance

### Settings
- Model selection (Qwen3, Llama3)
- Temperature adjustment
- Chunk size configuration
- Export preferences

---

## 📈 Visualizations Supported

- Line Charts (trends)
- Bar Charts (comparisons)
- Scatter Plots (correlations)
- Pie Charts (distributions)
- Histograms (distributions)
- Heatmaps (correlations)
- Box Plots (outliers)
- Area Charts (time-series)

---

## 🔧 Environment Configuration

Create `.env` file:

```env
# Backend
BACKEND_URL=http://localhost:8000
FRONTEND_URL=http://localhost:3000

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/rag_analytics
DATABASE_USER=user
DATABASE_PASSWORD=password

# JWT
SECRET_KEY=your-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

# Ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=qwen:7b

# Upload
MAX_UPLOAD_SIZE=104857600  # 100MB
UPLOAD_DIR=/tmp/uploads

# FAISS
VECTOR_DB_PATH=/tmp/faiss_db
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

# Logs
LOG_LEVEL=INFO
LOG_DIR=/tmp/logs
```

---

## 📚 Example Usage

### 1. Upload Dataset
```python
import requests

with open('sales_data.csv', 'rb') as f:
    files = {'file': f}
    response = requests.post(
        'http://localhost:8000/api/datasets/upload',
        files=files,
        headers={'Authorization': f'Bearer {token}'}
    )
    dataset_id = response.json()['id']
```

### 2. Ask Natural Language Query
```python
response = requests.post(
    'http://localhost:8000/api/chat/message',
    json={
        'dataset_id': dataset_id,
        'message': 'What are the top 5 products by revenue?',
        'model': 'qwen:7b'
    },
    headers={'Authorization': f'Bearer {token}'}
)
print(response.json())
```

### 3. Generate Forecast
```python
response = requests.post(
    'http://localhost:8000/api/analytics/forecast',
    json={
        'dataset_id': dataset_id,
        'column': 'revenue',
        'periods': 30,
        'method': 'prophet'
    },
    headers={'Authorization': f'Bearer {token}'}
)
forecast_data = response.json()
```

### 4. Detect Anomalies
```python
response = requests.post(
    'http://localhost:8000/api/analytics/anomalies',
    json={
        'dataset_id': dataset_id,
        'column': 'transactions',
        'method': 'isolation_forest',
        'contamination': 0.1
    },
    headers={'Authorization': f'Bearer {token}'}
)
anomalies = response.json()
```

### 5. Generate Report
```python
response = requests.post(
    'http://localhost:8000/api/reports/generate',
    json={
        'dataset_id': dataset_id,
        'title': 'Q1 2024 Analytics Report',
        'sections': ['summary', 'charts', 'insights', 'recommendations']
    },
    headers={'Authorization': f'Bearer {token}'}
)
report_url = response.json()['download_url']
```

---

## 🐳 Docker Deployment

### Development
```bash
docker-compose -f docker-compose.dev.yml up
```

### Production
```bash
docker-compose -f docker-compose.prod.yml up -d
```

### View Logs
```bash
docker-compose logs -f backend
docker-compose logs -f frontend
```

### Stop Services
```bash
docker-compose down
```

---

## 📊 Performance Optimization

- **Caching**: Redis for query results
- **Async Processing**: Celery for long-running tasks
- **Vector Index**: FAISS for fast semantic search
- **Database Indexing**: PostgreSQL indices on common queries
- **Connection Pooling**: SQLAlchemy connection pool
- **CDN**: Frontend assets via CDN

---

## 🛡️ Security Features

- JWT token-based authentication
- Password hashing (bcrypt)
- CORS configuration
- Input validation
- SQL injection prevention (parameterized queries)
- File upload validation
- Rate limiting
- Audit logging
- HTTPS support

---

## 📝 Logging & Monitoring

- Structured JSON logging
- Application metrics
- Error tracking
- Query performance monitoring
- User activity logs
- API usage analytics

---

## 🚀 Deployment to Production

### AWS EC2
```bash
# SSH into instance
ssh -i key.pem ubuntu@instance-ip

# Clone repo and setup
git clone https://github.com/Kravi21062/ai-rag-analytics.git
cd ai-rag-analytics

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Configure environment
cp .env.example .env
# Edit .env with production values

# Deploy
docker-compose -f docker-compose.prod.yml up -d

# Setup SSL with Let's Encrypt
sudo apt-get install certbot python3-certbot-nginx
sudo certbot certonly --standalone -d yourdomain.com
```

### Azure Container Instances
```bash
# Create container group
az container create \
  --resource-group myResourceGroup \
  --name rag-analytics \
  --image myregistry.azurecr.io/rag-analytics:latest
```

### Google Cloud Run
```bash
# Build and push
docker build -t gcr.io/PROJECT_ID/rag-analytics .
docker push gcr.io/PROJECT_ID/rag-analytics

# Deploy
gcloud run deploy rag-analytics \
  --image gcr.io/PROJECT_ID/rag-analytics \
  --platform managed
```

---

## 📚 Documentation

- [Architecture Guide](./docs/ARCHITECTURE.md)
- [API Documentation](./docs/API.md)
- [Setup Guide](./docs/SETUP.md)
- [Deployment Guide](./docs/DEPLOYMENT.md)
- [Development Guide](./docs/DEVELOPMENT.md)
- [Troubleshooting](./docs/TROUBLESHOOTING.md)

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Create a Pull Request

---

## 📄 License

MIT License - see LICENSE file for details.

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/Kravi21062/ai-rag-analytics/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Kravi21062/ai-rag-analytics/discussions)
- **Email**: support@example.com

---

## 🙏 Acknowledgments

- LangChain for LLM orchestration
- Ollama for local LLM execution
- FAISS for vector search
- Prophet for forecasting
- FastAPI for backend framework
- React for frontend framework

---

**Made with ❤️ by the AI Analytics Team**
