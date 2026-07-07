# NeuralFlow ⚡

**Plataforma de Automatización con Inteligencia Artificial**

NeuralFlow es una plataforma todo-en-uno que combina agentes de IA, automatización de tareas, scraping web, análisis de datos y más. Todo accesible via web, CLI, o Telegram.

## 🚀 Características

- **🤖 Agentes de IA** — Chat, web scraping, generación de contenido, análisis de datos
- **⚡ Automatización** — Programa tareas y flujos de trabajo con IA
- **🌐 Web Dashboard** — Panel de control moderno con Next.js
- **📱 Telegram Bot** — Interactúa con la plataforma desde Telegram
- **🖥️ CLI** — Herramienta de línea de comandos completa
- **🔐 Autenticación** — Sistema de usuarios con JWT
- **🐳 Docker** — Despliegue fácil con contenedores
- **📊 Analíticas** — Estadísticas de uso y rendimiento

## 🏗️ Estructura

```
neuralflow/
├── backend/          # FastAPI + agentes IA
├── web/              # Next.js dashboard
├── cli/              # CLI en Python
├── bot/              # Telegram bot
├── docs/             # Documentación
└── docker-compose.yml
```

## 🛠️ Stack

- **Backend:** FastAPI, SQLAlchemy, Celery, Groq AI
- **Frontend:** Next.js 14, Tailwind CSS, TypeScript
- **CLI:** Python, Click, Rich
- **Bot:** Python-telegram-bot
- **DB:** SQLite / PostgreSQL
- **Auth:** JWT + OAuth2

## 📦 Instalación Rápida

```bash
git clone https://github.com/Litios0912/neuralflow.git
cd neuralflow
cp .env.example .env
docker-compose up -d
```

## 📄 Licencia

MIT
