from typing import Iterator
from agno.agent import Agent, RunResponse 
from agno.models.ollama import Ollama 

agent = Agent(
    model=Ollama(id='gemma3:12b'),
    markdown=True
)

agent.print_response("Thời tiết Hà Nội ngày 14 tháng 3 năm 2025", stream=True)
