import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_plan(task: str) -> list[str]:

    prompt = f"""
Tu es un assitant spécialisé en décomposition de tâches en étapes claires.

Pour cela, tu vas décomposer la tâche donnée en étapes numérotées et séparées par **UN SEUL** \n.

Tâche :
{task}
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt }]
    ).choices[0].message.content


    tasks_list = []
    for resp in response.split("\n"):
        tasks_list.append(resp)

    return tasks_list
