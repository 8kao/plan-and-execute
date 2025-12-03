
# Plan & Execute Agent

### Agent autonome inspiré des approches Anthropic / OpenAI Agents, capable de :

- Décomposer automatiquement une tâche complexe  
- Choisir dynamiquement les outils nécessaires  
- Exécuter chaque étape de manière autonome  
- Accumuler et exploiter un contexte multi-étapes  
- Utiliser un moteur RAG interne (ChromaDB)  
- Produire une réponse finale synthétique  

---

## Fonctionnalités

### 1. Task Decomposition
Lorsqu’on pose une tâche complexe :

> "Analyse le module geometry et compare avec physics"

Le système :

- Analyse la demande  
- Génère des sous-tâches cohérentes  
- Produit une liste numérotée prête à l'exécution  

Exemple :

```
1.   Lister les fichiers du module geometry
    
2.   Lire le fichier principal
    
3.   Lister les fichiers du module physics
    
4.   Comparer les deux structures
    
5.   Rédiger une synthèse
```

### 2. Tool Selection

Le LLM choisit automatiquement quel outil utiliser pour chaque étape.

Outils disponibles :
- list_files : liste les fichiers d’un dossier 
- read_file : lit le contenu d’un fichier
- search : interrogation du RAG interne (ChromaDB)

> Possibilité de rajouter des tools dans `source/executor.py`

Le système détermine :

- Quel tool convient  
- Quel input lui passer  
- Quand utiliser le RAG  
- Quand réutiliser les résultats précédents

### 3. Déroulement de l'exécution 
Chaque étape du plan est réellement exécutée :

- Le tool choisi est appelé  
- Le résultat est capturé  
- Le résultat est ajouté au contexte global  
- Le système affiche chaque étape dans la console

### 4. Context Memory

Le système accumule :

- les résultats intermédiaires  
- les décisions précédentes  
- le contenu des fichiers lus  
- les outputs du RAG


## Installation

### 1. Installation des dépendances

  `pip install -r requirements.txt`

  

### 2. Ajouter la clé API OpenAI

Créer `.env` :

 `cp .env.example .env`

`OPENAI_API_KEY="votre_cle"`

## Ingestion

Places ton corpus de docs ou garde ceux déjà en place dans `data/docs_corpus`

Lance :

`python source/embed.py`

>Note : si vous souhaitez recréer une base vectorielle, il vous suffit de supprimer la base dans le fichier `data/vector_db` puis de relancer `python source/embed.py`

  
## Utilisation de l'app

Lance :

`python source/plan_and_execute.py`



