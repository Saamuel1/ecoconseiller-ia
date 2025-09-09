 EcoConseiller IA

Présentation
EcoConseiller IA est un agent intelligent développé dans une logique de numérique responsable, éthique et sobre. Il utilise la technologie RAG (Retrieval-Augmented Generation) pour fournir des réponses précises et sourcées à partir d'une base documentaire spécifique.

Conçu pour être modulaire et adaptable, l'agent peut être utilisé par toute équipe de Digital4Better pour gagner du temps, faciliter l'accès à l'information, et valoriser les pratiques écoresponsables.

---

Objectifs du projet
- Fournir un assistant IA souverain, alimenté uniquement par les documents choisis
- Accélérer la prise de décision écoresponsable grâce à une IA accessible
- Réduire la charge cognitive et le temps de recherche documentaire
- Permettre l'évolution rapide de l'agent vers d'autres cas d'usage internes

---

Fonctionnalités principales
| Fonctionnalité                | Description                                                        |
|-------------------------------|--------------------------------------------------------------------|
|Recherche intelligente | Recherche sémantique sur des documents PDF internes               |
|Réponses sourcées          | Chaque réponse est justifiée par un extrait + source + score      |
|Adaptable à tout domaine | Changez la base documentaire pour changer le domaine d'expertise |
|Historique                  | Historique local des questions/réponses sauvegardé automatiquement |
|Interface Streamlit      | Interface web simple, personnalisée aux couleurs de Digital4Better |



Fortes valeurs ajoutées pour nos équipes
| Problème                     | Solution via l'agent IA                                     |
|-----------------------------|-------------------------------------------------------------|
| Trop de documents à lire     | Synthèse instantanée + réponse ciblée                     |
| Difficulté à accéder à l'info | Accès direct à l'information fiable, sourcée              |
| Recherche fastidieuse       | Gain de temps, pas besoin de fouiller dans les fichiers    |
| Besoin d'IA éthique         | IA locale, souveraine, sur documents choisis               |

---

Adaptabilité maximale
Changer la base documentaire permet de créer instantanément :
- Un agent RH (avec documents RH internes)
- Un assistant qualité/sécurité (normes ISO, guides QHSE)
- Un support client IA (FAQ, guides, notices)
- Un assistant commercial (dossiers offres, références clients)

---

Structure technique
- Langage : Python 3
- IA générative : GPT-3.5 (ou autre LLM local possible)
- Recherche : FAISS + embeddings OpenAI
- Interface : Streamlit
- Base documentaire : fichiers PDF internes (ADEME, GreenConcept, etc.)

---

Installation rapide
1. Cloner le repo
2. Installer les dépendances : `pip install -r requirements.txt`
3. Créer un dossier `Documents/` avec vos fichiers PDF
4. Lancer : `streamlit run app.py`

---

Évolutions possibles
- Export PDF/CSV des réponses
- Feedback utilisateur pour améliorer l'agent
- IA locale sans API (ex : Mistral, Llama.cpp)
- Intégration Slack / Teams

---


