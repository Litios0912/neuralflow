import click
import httpx
import json
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from rich.prompt import Prompt
from rich.panel import Panel
from rich import box

console = Console()
API_URL = "http://localhost:8000"

class NeuralFlowClient:
    def __init__(self):
        self.token = None
        self.client = httpx.Client(base_url=API_URL, timeout=60)

    def login(self, email: str, password: str):
        resp = self.client.post("/auth/login", data={"username": email, "password": password})
        if resp.status_code == 200:
            data = resp.json()
            self.token = data["access_token"]
            self.client.headers["Authorization"] = f"Bearer {self.token}"
            console.print(f"[green]✅ Logged in as {data['user']['username']}[/green]")
            return True
        console.print(f"[red]❌ Login failed: {resp.json().get('detail', 'Unknown error')}[/red]")
        return False

    def register(self, email: str, username: str, password: str):
        resp = self.client.post("/auth/register", json={"email": email, "username": username, "password": password})
        if resp.status_code == 200:
            data = resp.json()
            self.token = data["access_token"]
            self.client.headers["Authorization"] = f"Bearer {self.token}"
            console.print(f"[green]✅ Registered as {data['user']['username']}[/green]")
            return True
        console.print(f"[red]❌ Registration failed: {resp.json().get('detail', 'Unknown error')}[/red]")
        return False

    def ensure_auth(self):
        if not self.token:
            console.print("[red]❌ Please login first: neuralflow login[/red]")
            return False
        return True

    def list_agents(self):
        if not self.ensure_auth(): return
        resp = self.client.get("/agents/")
        if resp.status_code == 200:
            agents = resp.json()
            if not agents:
                console.print("[yellow]No agents found. Create one with: neuralflow agent create[/yellow]")
                return
            table = Table(title="🤖 Agents", box=box.ROUNDED)
            table.add_column("ID", style="cyan")
            table.add_column("Name", style="green")
            table.add_column("Type", style="blue")
            table.add_column("Description")
            for a in agents:
                table.add_row(str(a["id"]), a["name"], a["type"], a.get("description", "")[:40])
            console.print(table)
        else:
            console.print(f"[red]Error: {resp.text}[/red]")

    def create_agent(self, name: str, agent_type: str, description: str = ""):
        if not self.ensure_auth(): return
        resp = self.client.post("/agents/", json={"name": name, "type": agent_type, "description": description, "config": {}})
        if resp.status_code == 200:
            data = resp.json()
            console.print(f"[green]✅ Agent '{data['name']}' created (ID: {data['id']})[/green]")
        else:
            console.print(f"[red]Error: {resp.json().get('detail', 'Unknown')}[/red]")

    def run_agent(self, agent_id: int, input_text: str):
        if not self.ensure_auth(): return
        with console.status("[bold green]Running agent..."):
            resp = self.client.post(f"/agents/{agent_id}/run", json={"input": input_text})
        if resp.status_code == 200:
            data = resp.json()
            console.print(Panel(data["output"], title=f"[bold]{data['agent_name']}[/bold] ({data['agent_type']})", border_style="blue"))
        else:
            console.print(f"[red]Error: {resp.json().get('detail', 'Unknown')}[/red]")

    def list_tasks(self):
        if not self.ensure_auth(): return
        resp = self.client.get("/tasks/")
        if resp.status_code == 200:
            tasks = resp.json()
            if not tasks:
                console.print("[yellow]No scheduled tasks[/yellow]")
                return
            table = Table(title="⏰ Scheduled Tasks", box=box.ROUNDED)
            table.add_column("ID", style="cyan")
            table.add_column("Name", style="green")
            table.add_column("Schedule", style="blue")
            table.add_column("Status")
            for t in tasks:
                table.add_row(str(t["id"]), t["name"], t["schedule_type"], t["status"])
            console.print(table)
        else:
            console.print(f"[red]Error: {resp.text}[/red]")

    def agent_types(self):
        if not self.ensure_auth(): return
        resp = self.client.get("/agents/types")
        if resp.status_code == 200:
            types = resp.json().get("agent_types", [])
            table = Table(title="Available Agent Types", box=box.ROUNDED)
            table.add_column("ID", style="cyan")
            table.add_column("Name")
            table.add_column("Description")
            for t in types:
                table.add_row(t["id"], t["name"], t["description"] or "")
            console.print(table)

client = NeuralFlowClient()

@click.group()
def cli():
    """NeuralFlow - AI Automation Platform CLI"""
    pass

@cli.command()
@click.option("--email", prompt=True)
@click.password_option()
def login(email, password):
    """Login to NeuralFlow"""
    client.login(email, password)

@cli.command()
@click.option("--email", prompt=True)
@click.option("--username", prompt=True)
@click.password_option()
def register(email, username, password):
    """Register a new account"""
    client.register(email, username, password)

@cli.group()
def agent():
    """Manage agents"""
    pass

@agent.command("list")
def list_agents():
    """List all agents"""
    client.list_agents()

@agent.command("types")
def list_types():
    """List available agent types"""
    client.agent_types()

@agent.command("create")
@click.option("--name", prompt=True)
@click.option("--type", "agent_type", prompt=True)
@click.option("--description", prompt=True, default="")
def create_agent(name, agent_type, description):
    """Create a new agent"""
    client.create_agent(name, agent_type, description)

@agent.command("run")
@click.argument("agent_id", type=int)
@click.argument("input_text")
def run_agent(agent_id, input_text):
    """Run an agent with input"""
    client.run_agent(agent_id, input_text)

@cli.group()
def task():
    """Manage scheduled tasks"""
    pass

@task.command("list")
def list_tasks():
    """List all scheduled tasks"""
    client.list_tasks()

@cli.command()
@click.argument("url")
def health(url="http://localhost:8000"):
    """Check API health"""
    try:
        resp = httpx.get(f"{url}/health", timeout=10)
        if resp.status_code == 200:
            console.print(f"[green]✅ API is healthy at {url}[/green]")
        else:
            console.print(f"[red]❌ API returned status {resp.status_code}[/red]")
    except Exception as e:
        console.print(f"[red]❌ Cannot connect: {e}[/red]")

if __name__ == "__main__":
    cli()
