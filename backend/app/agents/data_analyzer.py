"""Analizador y visualizador de datos"""
from app.agents.base import BaseAgent, AgentFactory
import json
import re

@AgentFactory.register("data_analyzer")
class DataAnalyzerAgent(BaseAgent):
    def run(self, input_data: str) -> str:
        data_blocks = re.findall(r'\{.*\}|\[.*\]', input_data, re.DOTALL)
        if not data_blocks:
            return "No JSON data found in input. Please provide data in JSON format."
        results = []
        for block in data_blocks[:3]:
            try:
                data = json.loads(block)
                if isinstance(data, list):
                    n = len(data)
                    keys = set()
                    for item in data:
                        if isinstance(item, dict):
                            keys.update(item.keys())
                    results.append(f"📊 Array Analysis:\n- Items: {n}\n- Fields: {', '.join(list(keys)[:10])}")
                    if data and isinstance(data[0], dict):
                        for key in list(keys)[:5]:
                            vals = [item.get(key) for item in data if isinstance(item, dict)]
                            numeric = [v for v in vals if isinstance(v, (int, float))]
                            if numeric:
                                results.append(f"  • {key}: min={min(numeric)}, max={max(numeric)}, avg={sum(numeric)/len(numeric):.2f}")
                elif isinstance(data, dict):
                    results.append(f"📊 Object Analysis:\n- Keys: {len(data)}\n- Top keys: {', '.join(list(data.keys())[:10])}")
            except json.JSONDecodeError:
                results.append("Invalid JSON data")
        return '\n'.join(results) if results else "No valid data found"
