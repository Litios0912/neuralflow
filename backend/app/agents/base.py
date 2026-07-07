from abc import ABC, abstractmethod

class BaseAgent(ABC):
    def __init__(self, config: dict = None):
        self.config = config or {}

    @abstractmethod
    def run(self, input_data: str) -> str:
        pass

class AgentFactory:
    _agents = {}

    @classmethod
    def register(cls, name: str):
        def wrapper(agent_class):
            cls._agents[name] = agent_class
            return agent_class
        return wrapper

    @classmethod
    def create_agent(cls, name: str, config: dict = None) -> BaseAgent:
        if name not in cls._agents:
            raise ValueError(f"Unknown agent type: {name}. Available: {list(cls._agents.keys())}")
        return cls._agents[name](config)

    @classmethod
    def get_available_types(cls) -> list:
        return [
            {"id": k, "name": v.__name__, "description": v.__doc__}
            for k, v in cls._agents.items()
        ]
