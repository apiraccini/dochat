# DOCHAT

This repository contains the proof of concept (POC) for creating a domain-specific RAG bot.

The process begins by collecting documents as strings in a Pandas DataFrame. Subsequently, the collection is embedded, with each document being chunked, using ChromaDB.
Upon receiving a query, the bot retrieves the most pertinent chunks based on their embedding distance from the query and passes them to the Language Model (LLM) as context, along with the original question.

The application runs in a docker-compose project, with one container for the application and one container for the database.

Starting from this project, a domain-specific RAG bot can be built by employing specific preprocessing functions to extract the required knowledge base format and defining any post-generation functions and behaviors.

## Usage guide

In order to start the application, copy and paste the following commands in your terminal (Docker Desktop must be running on your machine, and you also need to store your OpenAI API key in a `.env` file in the project root directory):

```
git clone https://github.com/apiraccini/dochat.git
cd datachat
docker-compose up
```

## TODO list

- [ ] Improve the embedding/retrieving steps (chunk size vs number of results).
- [ ] Implement control flows that filter query result based on a threshold distance.
- [ ] Use hallucination prompts to improve retrieval? See [here](https://cookbook.openai.com/examples/vector_databases/chroma/hyde-with-chroma-and-openai).
- [x] Add token length and cost estimation (with `tiktoken`).
- [ ] Make it a chatbot? With `langchain` or without?
