"""Asistente de chat con IA usando Groq"""
from app.agents.base import BaseAgent, AgentFactory
from app.config import settings
import httpx

@AgentFactory.register("chat")
class ChatAgent(BaseAgent):
    def run(self, input_data: str) -> str:
        system_prompt = self.config.get("system_prompt", "Eres un asistente AI útil y amigable.")
        model = self.config.get("model", "mixtral-8x7b-32768")
        api_key = self.config.get("api_key") or settings.GROQ_API_KEY
        if not api_key:
            return "Error: No GROQ API key configured."
        try:
            with httpx.Client(timeout=60) as client:
                resp = client.post(
                    "https://api.groq.com/openai/v1/chat/completions",
                    headers={"Authorization": f"Bearer {api_key}"},
                    json={
                        "model": model,
                        "messages": [
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": input_data}
                        ]
                    }
                )
                resp.raise_for_status()
                return resp.json()["choices"][0]["message"]["content"]
        except Exception as e:
            return f"Error: {str(e)}"
