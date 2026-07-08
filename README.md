# NeuralFlow ⚡

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12+-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-0.111-009688?style=for-the-badge&logo=fastapi" alt="FastAPI">
  <img src="https://img.shields.io/badge/Next.js-14-000000?style=for-the-badge&logo=next.js" alt="Next.js">
  <img src="https://img.shields.io/badge/TypeScript-5.4-3178C6?style=for-the-badge&logo=typescript" alt="TypeScript">
  <br>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker" alt="Docker">
  <img src="https://img.shields.io/badge/CI-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions" alt="CI">
  <img src="https://img.shields.io/badge/Telegram-Bot-26A5E4?style=for-the-badge&logo=telegram" alt="Telegram">
  <img src="https://img.shields.io/badge/CLI-Click-FFD43B?style=for-the-badge&logo=python" alt="CLI">
</p>

**Plataforma de Automatización con Inteligencia Artificial**

NeuralFlow es una plataforma todo-en-uno que combina agentes de IA, automatización de tareas, scraping web, análisis de datos y más. Todo accesible via Web, CLI o Telegram.

---

## 🚀 Características

| Característica | Descripción |
|---|---|
| 🤖 **Agentes de IA** | Chat, web scraping, generación de contenido, análisis de datos |
| ⚡ **Automatización** | Programa tareas y flujos de trabajo con scheduling |
| 🌐 **Web Dashboard** | Panel de control moderno con Next.js 14 + Tailwind |
| 📱 **Telegram Bot** | Interactúa con la plataforma desde Telegram |
| 🖥️ **CLI Completa** | Tool de línea de comandos con Rich (colores, tablas) |
| 🔐 **Autenticación** | Sistema de usuarios con JWT + OAuth2 |
| 🐳 **Docker Listo** | Despliegue fácil con docker-compose |
| 🔄 **CI/CD** | Integración continua con GitHub Actions |

## 🏗️ Stack Tecnológico

```
Frontend:  Next.js 14 + TypeScript + Tailwind CSS
Backend:   FastAPI + SQLAlchemy + Celery
IA:        Groq AI (mixtral-8x7b-32768)
CLI:       Python + Click + Rich
Bot:       python-telegram-bot 21.x
DB:        SQLite / PostgreSQL
Auth:      JWT + OAuth2
Deploy:    Docker + docker-compose
```

## 📦 Instalación Rápida

```bash
# 1. Clonar
git clone https://github.com/Litios0912/neuralflow.git
cd neuralflow

# 2. Configurar
cp .env.example .env
# Edita .env con tus API keys (GROQ_API_KEY, etc.)

# 3. Ejecutar con Docker
docker-compose up -d

# 4. Acceder
# Web:     http://localhost:3000
# API:     http://localhost:8000
# Docs:    http://localhost:8000/docs
```

## 🛠️ Instalación Manual

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Web
```bash
cd web
npm install
npm run dev
```

### CLI
```bash
cd cli
pip install -e .
neuralflow --help
```

### Bot
```bash
cd bot
pip install -r requirements.txt
python -m telegram.bot
```

## 🤖 Agentes de IA

| Tipo | Comando | Descripción |
|---|---|---|
| Chat | `chat` | Asistente conversacional con Groq AI |
| Web Scraper | `web_scraper` | Extrae contenido de sitios web |
| Content Generator | `content_generator` | Genera blogs, posts, emails y código |
| Data Analyzer | `data_analyzer` | Analiza datos JSON y obtén estadísticas |

## 🏗️ Estructura del Proyecto

```
neuralflow/
├── backend/          # FastAPI + Agentes IA
│   ├── app/
│   │   ├── api/      # Endpoints REST
│   │   ├── agents/   # Agentes de IA
│   │   ├── models/   # Modelos SQLAlchemy
│   │   └── services/ # Servicios (scheduler)
│   └── tests/        # Tests unitarios
├── web/              # Next.js Dashboard
│   ├── app/          # App Router pages
│   ├── components/   # Componentes React
│   └── lib/          # Utilidades API
├── cli/              # CLI en Python
├── bot/              # Telegram Bot
├── docs/             # Documentación
└── docker-compose.yml
```

## 📊 Estado del Proyecto

- [x] Backend FastAPI con 4 agentes IA
- [x] Autenticación JWT
- [x] Web Dashboard con Next.js
- [x] CLI tool interactiva
- [x] Telegram Bot
- [x] Docker deployment
- [x] CI/CD pipeline
- [x] Documentación completa
- [ ] Tests de integración
- [ ] Más agentes IA (imagen, video, audio)
- [ ] Despliegue en producción

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor abre un issue o PR.

## 📄 Licencia

MIT © 2026 Litios0912
