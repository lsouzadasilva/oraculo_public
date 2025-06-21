import os
from time import sleep
import streamlit as st
from langchain_community.document_loaders import (
    WebBaseLoader,
    CSVLoader,
    PyPDFLoader,
    TextLoader
)
from fake_useragent import UserAgent
from youtube_transcript_api import YouTubeTranscriptApi


def carrega_site(url):
    documento = ''
    for i in range(5):
        try:
            os.environ['USER_AGENT'] = UserAgent().random
            loader = WebBaseLoader(url, raise_for_status=True)
            lista_documentos = loader.load()
            documento = '\n\n'.join([doc.page_content for doc in lista_documentos])
            break
        except Exception as e:
            print(f'Erro ao carregar o site tentativa {i+1}: {e}')
            sleep(3)
    if documento == '':
        st.error('Não foi possível carregar o site')
        st.stop()
    return documento


def carrega_youtube(video_id):
    """
    Carrega a transcrição do vídeo do YouTube baseado no ID do vídeo.
    Exemplo de ID: para https://www.youtube.com/watch?v=MQjNdcnRLeE
    O ID é 'MQjNdcnRLeE'
    """
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['pt', 'en'])
        texto = " ".join([item['text'] for item in transcript])
        if texto.strip() == "":
            st.warning("Não foi possível obter a transcrição deste vídeo. Verifique se ele tem legendas disponíveis.")
        return texto
    except Exception as e:
        st.error(f"Erro ao obter transcrição do YouTube: {e}")
        st.stop()


def carrega_csv(caminho):
    loader = CSVLoader(caminho)
    lista_documentos = loader.load()
    documento = '\n\n'.join([doc.page_content for doc in lista_documentos])
    return documento


def carrega_pdf(caminho):
    loader = PyPDFLoader(caminho)
    lista_documentos = loader.load()
    documento = '\n\n'.join([doc.page_content for doc in lista_documentos])
    return documento


def carrega_txt(caminho):
    loader = TextLoader(caminho)
    lista_documentos = loader.load()
    documento = '\n\n'.join([doc.page_content for doc in lista_documentos])
    return documento
