# API Reference

## Authentication

### Register
```http
POST /auth/register
```

Request:
```json
{
  "email": "user@example.com",
  "username": "user",
  "password": "securepass123"
}
```

Response:
```json
{
  "access_token": "eyJ...",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "email": "user@example.com",
    "username": "user",
    "is_active": true
  }
}
```

### Login
```http
POST /auth/login
```

Request (form-data):
```
username: user@example.com
password: securepass123
```

### Get Current User
```http
GET /auth/me
Authorization: Bearer <token>
```

## Agents

### List Agents
```http
GET /agents/
Authorization: Bearer <token>
```

### Create Agent
```http
POST /agents/
Authorization: Bearer <token>
```

Request:
```json
{
  "name": "My Assistant",
  "type": "chat",
  "description": "My AI assistant",
  "config": {
    "system_prompt": "Eres un asistente útil",
    "model": "mixtral-8x7b-32768"
  }
}
```

### Run Agent
```http
POST /agents/{id}/run
Authorization: Bearer <token>
```

Request:
```json
{
  "input": "Hello, how are you?"
}
```

### Available Agent Types

| Type | Description |
|------|-------------|
| `chat` | AI Chat Assistant using Groq |
| `web_scraper` | Intelligent web scraping |
| `content_generator` | AI content generation |
| `data_analyzer` | JSON data analysis |

## Tasks

### List Tasks
```http
GET /tasks/
Authorization: Bearer <token>
```

### Create Task
```http
POST /tasks/
Authorization: Bearer <token>
```

## Health Check
```http
GET /health
```
