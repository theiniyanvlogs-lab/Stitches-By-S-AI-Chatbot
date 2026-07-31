from models.groq_model import get_llm

llm = get_llm()

response = llm.invoke("Say hello in one sentence.")

print("\nResponse:\n")
print(response.content)
