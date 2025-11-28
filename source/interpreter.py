import os
from openai import OpenAI
from dotenv import load_dotenv
import json


load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def interpret_steps(step: str, context: str) -> list[str]:

    prompt = f"""
Tu es un agent chargé de choisir la bonne action pour exécuter une étape d’un plan.

Voici les tools à ta disposition :

1. list_files(dir)
   - Retourne la liste des fichiers dans un dossier.

2. read_file(path)
   - Lit le contenu d’un fichier texte.

3. search(query)
   - Effectue une recherche RAG dans les documents indexés.

Étape à exécuter :
"{step}"

Contexte disponible :
{context}

Tu dois répondre STRICTEMENT en JSON avec ce format :

{{
    "tool": "<nom du tool>",
    "input": "<argument string ou liste>"
}}

Aucune explication. Aucun texte supplémentaire.
Seulement le JSON.
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    ).choices[0].message.content.strip()
    
    try:
        parsed = json.loads(response)
    except:
        raise ValueError(f"Réponse invalide du LLM :\n {response}\nFormat attendue : JSON")

    return parsed["tools"], parsed["input"]
