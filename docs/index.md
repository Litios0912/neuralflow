# NeuralFlow Documentation

Welcome to NeuralFlow - the AI Automation Platform.

## Quick Start

### Prerequisites
- Python 3.10+
- Node.js 18+
- Docker (optional)

### Installation

1. Clone the repo:
```bash
git clone https://github.com/Litios0912/neuralflow.git
cd neuralflow
```

2. Set up environment:
```bash
cp .env.example .env
# Edit .env with your API keys
```

3. Run with Docker:
```bash
docker-compose up -d
```

4. Access the platform:
- Web: http://localhost:3000
- API: http://localhost:8000
- Docs: http://localhost:8000/docs

### Manual Setup

#### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

#### Web
```bash
cd web
npm install
npm run dev
```

#### CLI
```bash
cd cli
pip install -e .
neuralflow --help
```

## Architecture

NeuralFlow is built with a microservices architecture:

```
┌─────────┐     ┌──────────┐     ┌──────────┐
│  Web UI │────▶│  FastAPI │────▶│ SQLiteDB │
│ (Next.js)│     │ Backend  │     │          │
└─────────┘     └──────────┘     └──────────┘
                      │
           ┌──────────┼──────────┐
           ▼          ▼          ▼
      ┌────────┐ ┌────────┐ ┌────────┐
      │  CLI   │ │Telegram│ │Agents  │
      │  Tool  │ │  Bot   │ │  IA    │
      └────────┘ └────────┘ └────────┘
```

## Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | JWT secret key | - |
| `DATABASE_URL` | Database URL | sqlite:///./neuralflow.db |
| `GROQ_API_KEY` | Groq AI API key | - |
| `TELEGRAM_BOT_TOKEN` | Telegram bot token | - |

## License

MIT
