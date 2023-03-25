import openai
import speech_recognition as sr
import pyaudio

openai.api_key = "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"

chunk = 1024
sample_format = pyaudio.paInt16
channels = 2
fs = 44100
seconds = 3.5
filename = "audio_file.wav"
messages = []
system_msg = "A partir de agora, você é um carrinho robô feito com Arduino. Você deve responder somente com os símbolos '1', '2', '3' e '4', tem que ser exatamente da forma que escrevi, tem que ser exatamente igual.\n \n o símbolo '3' significa ir para a esquerda.\n o símbolo '4' significa ir para a direita.\n o símbolo '1' significa ir para frente.\no símbolo '2' significa ir para trás.\n\nNenhuma outra resposta em nenhuma hipótese será permitida além desses símbolos, seja consistente nas respostas. Entendido?"

messages.append({"role": "system", "content": system_msg})
