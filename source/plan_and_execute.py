import os
from openai import OpenAI
from dotenv import load_dotenv
from executor import read_file, list_files, search_rag, AVAILABLE_TOOLS

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def plan_and_execute():
    