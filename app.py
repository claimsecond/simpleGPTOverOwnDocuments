import os
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
from dotenv import load_dotenv
load_dotenv()
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

if os.path.exists(os.environ["INDEX_FILE"]): 
    storage_context = StorageContext.from_defaults(persist_dir=os.environ["INDEX_FILE"])
    index = load_index_from_storage(storage_context)
else:
    documents = SimpleDirectoryReader(input_dir=os.environ["LOAD_DIR"]).load_data()
    index = GPTVectorStoreIndex.from_documents(documents)
    index._storage_context.persist(os.environ["INDEX_FILE"])

query_engine = index.as_query_engine()
print(query_engine.query("Summarize the book in 10 sentences?"))