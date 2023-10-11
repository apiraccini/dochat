import time
import os
import chromadb
import pandas as pd
from chromadb.config import Settings
import openai
from dotenv import load_dotenv

from .misc import estimate_cost, filter_result


def ask(question):

    corpus = load_corpus()
    
    raw_result = corpus.query(query_texts=f'{question}', n_results=3)
    result = filter_result(raw_result)

    context = ' '.join([f'DOC: {id}\nCONTENT: {document}\n\n' for id, document in zip(result['ids'][0], result['documents'][0])])
    context = context.rstrip('\n')
    
    prompt = [
        {'role': 'system', 'content': "Take a deep breath and answer the following question based on the context provided. If you can't find any evidence, say you don't know."},
        {'role': 'user', 'content': f"Question: {question}. \nThe context, written in markdown syntax, is the following:\n<<<{context}>>>\n. Anwer:"}
    ]
    
    response =  gpt_response(prompt)
    prompt_string =  ' '.join([str(d) for d in prompt])
    log =  estimate_cost(prompt)
    
    return response, prompt_string, log


def gpt_response(prompt):

    load_dotenv()
    openai.api_key = os.environ['OPENAI_API_KEY']

    response = openai.ChatCompletion.create(
            model = 'gpt-3.5-turbo',
            messages = prompt,
            max_tokens = 512,
            temperature = 0.2
        ).choices[0].message.content

    return response


def load_corpus(name='corpus', chunk_size=3000):

    while True:
        try:
            chroma_client = chromadb.HttpClient(host="chroma", port="8000", settings=Settings(allow_reset=True, anonymized_telemetry=False))
            break
        except chromadb.exceptions.ConnectionError:
            print("ChromaDB not available yet, waiting...")
            time.sleep(5)
    
    try:
        corpus = chroma_client.get_collection(name)
    except:
        corpus = chroma_client.create_collection(name)
        df = pd.read_csv('data/processed/text_df.csv')

        for _, row in df.iterrows():
            
            text = row['article']
            chunked_text = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
            chunked_ids = [f"{str(row['id'])}_chunk_{idx+1}" for idx in range(len(chunked_text))]

            corpus.add(
                ids=chunked_ids,
                documents=chunked_text
            ) 
    
    return corpus