from pathlib import Path

from agno.agent import Agent
from agno.media import Image
from agno.models.ollama import Ollama

agent = Agent(
    model=Ollama(id="gemma3:4b"),
    markdown=True,
)

image_path = Path(__file__).parent.joinpath("anh-ha-noi-17.jpg")
print(image_path, end="\n\n================")
agent.print_response(
    "Write a 3 sentence fiction story about the image",
    images=[Image(filepath=image_path)],
)
