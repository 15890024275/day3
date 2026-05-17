from dataclasses import dataclass


@dataclass
class AgentState():
    messages:str
    memory:str

    def run(self):
        pass

