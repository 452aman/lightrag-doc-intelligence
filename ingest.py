from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


def load_pdf(file_path):
    loader = PyPDFLoader(file_path)   # what does it need?
    pages = loader.load()       # this one I'll give you
    return pages

def split_documents(pages):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, 
        chunk_overlap=50
    )
    chunks = text_splitter.split_documents(pages)
    return chunks

def ingest_pdf(file_path):
    pages = load_pdf(file_path)
    chunks = split_documents(pages)
    return chunks