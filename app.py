import streamlit as st
from agent import ask_agent
from retriever import load_and_split_documents
import os
import csv

# --- Configuration page ---
st.set_page_config(page_title="EcoConseiller IA - Digital4Better", layout="wide")

col1, col2 = st.columns([1, 9])
with col2:
    st.title("EcoConseiller IA")
    st.subheader("par Samuel Duarte Dos Santos")

st.markdown("---")

# --- Filtrer la source ---
st.markdown("#### Filtrer la source documentaire (optionnel)")
_, Doc_from_folder = load_and_split_documents()
Doc_from_folder.insert(0, 'Tous les documents')
selected_doc = st.selectbox("", Doc_from_folder)

# --- Question ---
st.markdown("#### Posez votre question")
question = st.text_input("Ex : Comment réduire l'empreinte carbone d’un site web ?", "")

# --- Historique (helpers) ---
history_file = "logs/streamlit_history.csv"
os.makedirs("logs", exist_ok=True)

@st.cache_data
def read_history(path: str):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return list(csv.reader(f))

def append_history(path: str, q: str, r: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([q, r])
    # invalide le cache pour que l'UI reflète le nouvel état
    read_history.clear()

def clear_history(path: str):
    if os.path.exists(path):
        try:
            os.remove(path)
        except PermissionError:
            # Sur Windows, s'il y avait un handle ouvert : tentative fallback
            with open(path, "w", encoding="utf-8") as f:
                f.write("")
    read_history.clear()

# --- Traitement IA ---
if st.button("Obtenir une réponse") and question.strip():
    with st.spinner("Recherche en cours..."):
        response, contexts = ask_agent(question, selected_doc)

    st.markdown("### Réponse personnalisée :")
    st.success(response)

    st.markdown("### Sources utilisées :")
    for i, ctx in enumerate(contexts):
        with st.expander(f"Source {i+1} — {ctx['source']} (Score : {ctx['score']:.4f})"):
            st.text(ctx['content'])

    # Historique CSV
    append_history(history_file, question, response)

st.markdown("---")
st.markdown("### Historique des interactions")

rows = read_history(history_file)
if rows:
    for i, row in enumerate(reversed(rows)):
        q, r = (row + ["", ""])[:2]  # garde au moins 2 champs
        with st.expander(f"Question {i+1} : {q}"):
            st.write(f"Réponse : {r}")
else:
    st.info("Aucune interaction pour le moment.")

# --- Effacer l’historique ---
if st.button("Effacer l’historique"):
    clear_history(history_file)
    st.success("Historique supprimé.")
    # force le rafraîchissement de l’UI après suppression
    try:
        st.rerun()
    except Exception:
        st.experimental_rerun()

# --- Footer ---
st.markdown("---")
