from agno.agent import Agent, RunResponse 
from agno.models.ollama import Ollama 

agent = Agent(
    model=Ollama(id='gemma3:4b'),
    markdown=True
)

agent.print_response("Kể một câu chuyện cười")