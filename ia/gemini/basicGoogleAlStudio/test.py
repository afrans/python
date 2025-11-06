from google import genai

client = genai.Client(api_key="AIza...")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works in a few words",
)

print(
    response.text
)  # Computers learning from data to recognize patterns and make decisions.

""" Criar conta e pegar API Key
Vá para Google AI Studio: https://ai.google.com/studio/
Entre com sua conta Google.
Vá em "Get API key" → "Create API key in new project".
Guarde a chave que aparecer (é parecida com AIza...). """
