from agno.agent import Agent
from dotenv import load_dotenv
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

load_dotenv(dotenv_path='../.env')

agent = Agent(
    model = OpenAIChat(id="gpt-3.5-turbo", temperature=0.1),
    description="bạn là một người hài hước, nói chuyện theo phong cách hài hước.",
    markdown=True,
    tools=[DuckDuckGoTools()],
    show_tool_calls=True
)

agent.print_response("Nói cho tôi nhưng tin nóng ở Hà Nội ngày hôm nay.", stream=True)