from typing import Iterator
from agno.agent import Agent, RunResponse 
from agno.models.openai import OpenAIChat 
from agno.utils.pprint import pprint_run_response 
from dotenv import load_dotenv 
load_dotenv(dotenv_path='.env')

agent = Agent(model=OpenAIChat(id="gpt-3.5-turbo"))

response: RunResponse = agent.run("Kể cho tôi một câu chuyện ngắn buôn cười")

response_stream: Iterator[RunResponse] = agent.run("Kể cho tôi một câu chuyện bi hài")

pprint_run_response(response, markdown=True)

pprint_run_response(response_stream, markdown=True)