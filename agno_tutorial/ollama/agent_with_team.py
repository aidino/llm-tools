from typing import Iterator
from agno.agent import Agent, RunResponse 
from agno.models.ollama import Ollama
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=Ollama(id='qwen2.5:3b'),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True
)

agent.print_response("Tin tức bất động sản Hà Nội ngày 14 tháng 3 năm 2025", stream=True)
