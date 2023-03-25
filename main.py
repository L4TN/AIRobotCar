from config import messages
from record_audio import record_audio
from speech_to_text import speech_to_text
from assitantAI import assistant_response, extract_directions
from bot_controller import start_robot, typing_robot

print("Seu novo assistente está pronto!")
start_robot()
while True:
    record_audio()

    try:
        text = speech_to_text()
    except:
        print("houve exception")
        continue

    message = text if text else None

    if message is not None:
        reply = assistant_response(message)
        directions = extract_directions(reply)
        print("Direções encontradas: ", directions)
        typing_robot(directions)
