from pynput import keyboard
import pyperclip
from ollama import chat

from prompts import FIX_TYPOS_PROMPT
from ollama_models import MISTRAL_K_S

controller = keyboard.Controller()

f8 = keyboard.Key.f8.value


def fix_text(text):
    prompt = FIX_TYPOS_PROMPT.substitute(text=text)
    stream = chat(
        model=MISTRAL_K_S,
        messages=[
        {
            'role': 'user',
            'content': prompt,
            'keep_alive': "5m"
        }],
        stream=True,
    )

    return stream


def fix_selection():
    with controller.pressed(keyboard.Key.ctrl):
        controller.tap('c')

    text = pyperclip.paste()   
    stream = fix_text(text)

    for chunk in stream:
        pyperclip.copy(chunk['message']['content'])
        with controller.pressed(keyboard.Key.ctrl):
            controller.tap('v')


def on_f8():
    print("f8 was pressed")
    fix_selection()


with keyboard.GlobalHotKeys({
        f"{f8}": on_f8}) as h:
    h.join()
