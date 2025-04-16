# inclusao das bibliotecas
import os # biblioteca de funçoes do sistema operacional
from typing import List # biblioteca para criar uma lista
# Bibliotecas para ler os diretorio do pdf
from llama_index.core import SimpleDirectoryReader, StorageContext, VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter # biblioteca para separar as informações do pdf e dividir
from llama_index.embedding.huggingface import HuggingFaceEmbedding # bibliote
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.llms.groq import Groq
from llama_index.core.memory import ChatSummaryMemoryBuffer