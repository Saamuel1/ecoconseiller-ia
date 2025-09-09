#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  2 14:09:47 2025

@author: duarteds
"""

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

from dotenv import load_dotenv

load_dotenv()
embeddings = OpenAIEmbeddings(openai_api_key=os.environ["OPENAI_API_KEY"])

# Chemin du dossier de documents
DOC_DIR = "Documents/"


def load_and_split_documents():
    """Charge tous les .pdf du dossier DOC_DIR et les découpe en chunks."""
    list_pour_interface = []
    all_docs = []
    for filename in os.listdir(DOC_DIR):
        if filename.endswith(".pdf"):
            list_pour_interface.append(filename)
            file_path = os.path.join(DOC_DIR, filename)
            docs = PyPDFLoader(file_path).load()
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=500,
                chunk_overlap=50, # Quoi dupliquer pour garder du contexte
                separators=["\n\n", "\n", ".", "!", "?", ",", " "] # Spécifie où couper proprement
            )
            split_docs = splitter.split_documents(docs)

            # Ajout du nom du fichier comme métadonnée
            for doc in split_docs:
                parts = filename.replace(".pdf", "").split("_")
                doc.metadata["source"] = filename
                doc.metadata["auteur"] = parts[0]
                doc.metadata["type"] = parts[1]
                doc.metadata["date"] = parts[2]
            all_docs.extend(split_docs)
    return all_docs, list_pour_interface

def build_vectors():
    """Crée un index FAISS à partir des documents."""
    docs_after_split, _ = load_and_split_documents() # On retourne la liste de tous les chunks
    embeddings = OpenAIEmbeddings() # Utilisation de GPT 3.5 pour transformer du texte en vecteur numérique
    vectors_store = FAISS.from_documents(docs_after_split, embeddings) # Transforme le texte puis stocke tous les vecteurs dans un index FAISS
    return vectors_store

vectors_store = build_vectors()

def search_similarity(question: str, k, source_docs: str = "Tous les documents") -> list:
    results = vectors_store.similarity_search_with_score(question, k=20)
    results = sorted(results, key=lambda x: x[1])  # score croissant

    contexte = []
    seen_sources = set()

    for doc, score in results:
        source = doc.metadata.get("source", "inconnu")
        if source_docs != "Tous les documents" and source_docs.lower() not in source.lower():
            continue  # skip non-matching source
        if source not in seen_sources:
            contexte.append({
                "content": doc.page_content.strip(),
                "source": source,
                "date": doc.metadata.get("date", "inconnue"),
                "score": score
            })
            seen_sources.add(source)
        if len(contexte) >= k:
            break

    return contexte


















