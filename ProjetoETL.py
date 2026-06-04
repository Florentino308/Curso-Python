import json
import openai

client = openai.OpenAI()

users = [
    {
        "id": 1,
        "name": "Manuela Mendes",
        "account": {"number": "00001-1", "agency": "0001", "balance": 150.0, "limit": 500.0},
        "card": {"number": "**** **** **** 1111", "limit": 1000.0},
        "news": []
    },
    {
        "id": 2,
        "name": "Antônio Silva",
        "account": {"number": "00002-2", "agency": "0001", "balance": 320.0, "limit": 500.0},
        "card": {"number": "**** **** **** 2222", "limit": 1000.0},
        "news": []
    },
    {
        "id": 3,
        "name": "José Medeiros",
        "account": {"number": "00003-3", "agency": "0001", "balance": 80.0, "limit": 500.0},
        "card": {"number": "**** **** **** 3333", "limit": 1000.0},
        "news": []
    },
    {
        "id": 4,
        "name": "Laís Pereira",
        "account": {"number": "00004-4", "agency": "0001", "balance": 500.0, "limit": 1000.0},
        "card": {"number": "**** **** **** 4444", "limit": 2000.0},
        "news": []
    },
    {
        "id": 5,
        "name": "Olívia Nunes",
        "account": {"number": "00005-5", "agency": "0001", "balance": 1200.0, "limit": 2000.0},
        "card": {"number": "**** **** **** 5555", "limit": 5000.0},
        "news": []
    },
]

print("=" * 60)
print("EXTRACT — dados carregados com sucesso")
print(f"Total de clientes: {len(users)}")
print("=" * 60)

def generate_ai_news(user: dict) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Modelo recomendado da OpenAI
        max_tokens=200,
        messages=[
            {
                "role": "system", 
                "content": "Você é um especialista em marketing bancário."
            },
            {
                "role": "user",
                "content": (
                    f"Crie uma mensagem para {user['name']} sobre a importância dos "
                    f"investimentos (máximo de 100 caracteres). Responda apenas com a "
                    f"mensagem, sem aspas ou explicações adicionais."
                )
            }
        ]
    )
    return response.choices[0].message.content.strip().strip('"')


print("\nTRANSFORM — gerando mensagens personalizadas...\n")

for user in users:
    news_text = generate_ai_news(user)
    print(f"  {user['name']:10s} → {news_text}")
    user["news"].append({
        "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
        "description": news_text
    })

print("\n" + "=" * 60)
print("TRANSFORM — mensagens geradas com sucesso")
print("=" * 60)

output_path = "output_users.json"

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(users, f, ensure_ascii=False, indent=2)

print(f"\nLOAD — dados salvos em '{output_path}'")
print("=" * 60)
print("\nResultado final:\n")
print(json.dumps(users, ensure_ascii=False, indent=2))