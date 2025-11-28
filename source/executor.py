import os
from openai import OpenAI
from dotenv import load_dotenv
from retriever import retrieve_context

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def list_files(path: str):

    result = []

    for root, dirs, files in os.walk(path):
        for f in files:
            result.append(os.path.join(root, f))

    return result
    
def read_file(path: str):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read
    except:
        return ""

def search_rag(query: str):

    return retrieve_context(query, k=5)

def execute_step(tool: str, input: str):

    AVAILABLE_TOOLS  = {
        "list_files": list_files,
        "read_file": read_file,
        "search": search_rag
    }
    
    if tool not in AVAILABLE_TOOLS:
        return f"Tool inconnu : {tool}" 

    tool = AVAILABLE_TOOLS[tool]

    try:
        if isinstance(tool, list):
            results = []
            for i in input:
                out = tool(i)
                if isinstance(out, list):
                    out = "\n".join(out)
                    results.append(out)
            return "\n---\n".join(results)
        
        result = tool(input)

        if isinstance(result, list):
            return "\n".join(result)

        return str(result)

    except Exception as e:
        return f"Exception lors de l'exécution de {tool}: {e}"
