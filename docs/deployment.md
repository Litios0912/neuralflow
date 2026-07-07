# Deployment Guide

## Docker Deployment (Recommended)

```bash
# Clone and configure
git clone https://github.com/Litios0912/neuralflow.git
cd neuralflow
cp .env.example .env
nano .env  # Configure your API keys

# Start all services
docker-compose up -d

# Check logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Services
| Service | Port | Description |
|---------|------|-------------|
| Backend | 8000 | FastAPI + Agents |
| Web | 3000 | Next.js Dashboard |
| Bot | - | Telegram Bot |

## Manual Deployment

### Backend (FastAPI)
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Web (Next.js)
```bash
cd web
npm install
npm run build
npm start
```

### CLI
```bash
cd cli
pip install -e .
```

## Environment Variables

Create a `.env` file:

```bash
SECRET_KEY=your-random-secret-key-here
DATABASE_URL=sqlite:///./neuralflow.db
GROQ_API_KEY=gsk_your_groq_api_key
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Production Considerations

- Use PostgreSQL instead of SQLite for production
- Set up proper secrets management
- Configure CORS for your domain
- Use a reverse proxy (nginx) for production
- Enable HTTPS with Let's Encrypt
