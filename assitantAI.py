from config import messages
import openai as ai
import time

def assistant_response(text):
    if text:
        messages.append({"role": "user", "content": text})
        max_attempts = 5
        attempts = 0

        while attempts < max_attempts:
            try:
                print("Enviando Request")
                response = ai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages,
                    timeout=3  # Timeout em segundos
                )
                print("Request recebida")
                reply = response["choices"][0]["message"]["content"]
                messages.append({"role": "assistant", "content": reply})
                return reply
            except ai.OpenAI.TimeoutError:
                print("Erro API")
                attempts += 1
                if attempts >= max_attempts:
                    print("Tentativas esgotadas. A API demorou muito para responder.")
                    return None
                time.sleep(2)  # Pausa de 2 segundos antes de tentar novamente
    return None

def extract_directions(reply):
    directions = []
    pos = 0

    while pos < len(reply):
        current_symbol = reply[pos]
        if current_symbol in ["1", "2", "3", "4"]:
            directions.append(current_symbol)
            pos += 1
        else:
            pos += 1

    return directions




