from agno.agent import Agent 
from agno.models.openai import OpenAIChat 
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')

web_agent = Agent(
    name='Web Agent',
    role="Search the web for information",
    model=OpenAIChat(id="gpt-3.5-turbo"),
    tools=[DuckDuckGoTools()],
    instructions="Alway include the source",
    show_tool_calls=True,
    markdown=True,
    debug_mode=True
)

finance_agent = Agent(
    name="Finance agent",
    role="Get financial data",
    model=OpenAIChat(id="gpt-3.5-turbo"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    instructions="Use table to display data",
    show_tool_calls=True,
    markdown=True,
    debug_mode=True
)

agent_team = Agent(
    team=[web_agent, finance_agent],
    model=OpenAIChat(id="gpt-3.5-turbo"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True, 
    monitoring=True
)

agent_team.print_response("What's the market outlook and financial performance of AI semiconductor companies?", stream=True)