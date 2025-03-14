import os 
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.embedder.openai import OpenAIEmbedder
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.vectordb.lancedb import LanceDb, SearchType

load_dotenv(dotenv_path='../.env')

agent = Agent(
    model=OpenAIChat(id="gpt-3.5-turbo", temperature=0.1),
    description='Bạn là một chuyên viên hướng dẫn khách hàng sử dụng phần mềm.',
    instructions=[
        'Tìm kiếm thông tin từ hướng dẫn sủe dụng phần mềm VNEID',
        'Nếu câu hỏi cần tìm kiếm thông tin cập nhật trên mạng internet thì hãy tìm kiếm trên web và trả lời dựa trên đó',
        'Ưu tiên kiến thức trong tài liệu knowledge base, tài liệu đính kèm hơn là tìm kiếm trên internet'
    ],
    knowledge=PDFKnowledgeBase(
        path='data/huong-dan-su-dung-vneid.pdf', 
        vector_db=LanceDb(
            uri='temp/lancedb',
            table_name='vneid',
            search_type=SearchType.hybrid,
            embedder=OpenAIEmbedder(id='text-embedding-3-small'),
        ),
    ),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True
)

if agent.knowledge is not None:
    agent.knowledge.load()


agent.print_response("Các bước để đăng ký định danh mức 2")
