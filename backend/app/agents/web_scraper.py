"""Agente de web scraping inteligente"""
from app.agents.base import BaseAgent, AgentFactory
import httpx
from bs4 import BeautifulSoup
import re

@AgentFactory.register("web_scraper")
class WebScraperAgent(BaseAgent):
    def run(self, input_data: str) -> str:
        urls = re.findall(r'(https?://\S+)', input_data)
        if not urls:
            return "Please provide a URL to scrape."
        results = []
        for url in urls[:3]:
            try:
                with httpx.Client(timeout=30, follow_redirects=True) as client:
                    resp = client.get(url, headers={"User-Agent": "Mozilla/5.0"})
                    resp.raise_for_status()
                    soup = BeautifulSoup(resp.text, 'html.parser')
                    for tag in soup(['script', 'style', 'nav', 'footer', 'header']):
                        tag.decompose()
                    text = soup.get_text(separator='\n', strip=True)
                    lines = [line for line in text.split('\n') if len(line.strip()) > 30]
                    content = '\n'.join(lines[:50])
                    results.append(f"=== {url} ===\n{content[:2000]}")
            except Exception as e:
                results.append(f"Error scraping {url}: {str(e)}")
        return '\n\n'.join(results)
