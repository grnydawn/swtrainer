# generate_code.py
from langchain_community.llms import Ollama

def generate_code(prompt):
    llm = Ollama(model="llama3")
    response = llm.invoke(prompt)
    return response

if __name__ == "__main__":
    prompt = "Write a Python function to calculate the factorial of a number."
    code = generate_code(prompt)
    print(code)

