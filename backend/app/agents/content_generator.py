"""Generador de contenido con IA usando Groq"""
from app.agents.base import BaseAgent, AgentFactory
from app.config import settings
import httpx

@AgentFactory.register("content_generator")
class ContentGeneratorAgent(BaseAgent):
    def run(self, input_data: str) -> str:
        content_type = self.config.get("type", "blog")
        tone = self.config.get("tone", "professional")
        length = self.config.get("length", "medium")
        api_key = self.config.get("api_key") or settings.GROQ_API_KEY
        if not api_key:
            return "Error: No GROQ API key configured."
        prompts = {
            "blog": "Escribe un artículo de blog",
            "social": "Escribe un post para redes sociales",
            "email": "Escribe un email profesional",
            "code": "Escribe código",
        }
        type_prompt = prompts.get(content_type, "Escribe contenido")
        system = f"Eres un experto creador de contenido. {type_prompt} con tono {tone}. {'Extiende bien el contenido.' if length == 'long' else 'Sé conciso.' if length == 'short' else ''}"
        try:
            with httpx.Client(timeout=60) as client:
                resp = client.post(
                    "https://api.groq.com/openai/v1/chat/completions",
                    headers={"Authorization": f"Bearer {api_key}"},
                    json={
                        "model": "mixtral-8x7b-32768",
                        "messages": [
                            {"role": "system", "content": system},
                            {"role": "user", "content": input_data}
                        ]
                    }
                )
                resp.raise_for_status()
                return resp.json()["choices"][0]["message"]["content"]
        except Exception as e:
            return f"Error: {str(e)}"
