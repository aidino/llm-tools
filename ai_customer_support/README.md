# 🛒 AI Customer Support Agent with Memory

Ứng dụng Streamlit này triển khai một đại lý hỗ trợ khách hàng được hỗ trợ bởi AI cho dữ liệu tổng hợp được tạo bằng GPT-4o. Agent sử dụng mô hình GPT-4o của OpenAI và duy trì bộ nhớ về các tương tác trước đây bằng thư viện Mem0 với Qdrant làm vector store.

Tính năng

* Giao diện trò chuyện để tương tác với đại lý hỗ trợ khách hàng AI
* Bộ nhớ liên tục về tương tác và hồ sơ khách hàng
* Tạo dữ liệu tổng hợp để thử nghiệm và trình diễn
* Sử dụng mô hình GPT-4o của OpenAI để đưa ra phản hồi thông minh.

### Requirements dependencies

```bash
streamlit 
openai
mem0ai
```

### Run `Qdrant` vector store

```bash
docker pull qdrant/qdrant

docker run -p 6333:6333 -p 6334:6334 \
    -v "$(pwd)/qdrant_storage:/qdrant/storage:z" \
    qdrant/qdrant
```

### Run the agent

```bash
streamlit run customer_support_agent.py
```