#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Aug  2 14:09:47 2025

@author: duarteds
"""


"""
EcoConseiller IA — Appel simple à GPT-3.5 avec nouvelle API OpenAI
"""

# agent.py

import openai
from retriever import search_similarity
import os
from datetime import datetime
import csv

# Récupération de la clé API (depuis .env si nécessaire)
openai.api_key = os.getenv("OPENAI_API_KEY")

def call_openai(prompt: str) -> str:
    """Appelle le modèle GPT-3.5 avec un prompt donné."""
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Tu es un conseiller numérique responsable, clair et pédagogique."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=500
    )
    return response.choices[0].message.content

def ask_agent(question: str, source_docs: str = "Tous les documents"):
    contexts = search_similarity(question, k=5, source_docs=source_docs)
    context_str = ""
    for i, ctx in enumerate(contexts):
        context_str += f"[Source: {ctx['source']}, Score: {ctx['score']:.4f}]\n{ctx['content']}\n\n"

    prompt = (
        f"Voici des extraits de documents sur le numérique responsable :\n\n"
        f"{context_str}\n"
        f"En te basant uniquement sur ces extraits, réponds de manière claire à la question suivante :\n"
        f"{question}"
    )

    response = call_openai(prompt)
    log_interaction(question, response)
    return response, contexts


def log_interaction(question: str, response: str):
    """Enregistre la question et la réponse dans un fichier CSV."""
    os.makedirs("logs", exist_ok=True)
    with open("logs/interactions.csv", "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([datetime.now().isoformat(), question, response])



