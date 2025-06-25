import tkinter as tk
from pynput import keyboard
import pyperclip
from ollama import chat

from prompts import FIX_TYPOS_PROMPT, TRANSLATE_TO_UKRAINIAN_PROMPT
from ollama_models import MISTRAL_K_S
from windows.text_window import TextStreamWindow


controller = keyboard.Controller()

f7 = keyboard.Key.f7.value
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


def translate_text(text):
    prompt = TRANSLATE_TO_UKRAINIAN_PROMPT.substitute(text=text)
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


def show_translation_in_ui():
    with controller.pressed(keyboard.Key.ctrl):
        controller.tap('c')

    text = pyperclip.paste()   
    stream = translate_text(text)

    root = tk.Tk()
    window = TextStreamWindow(root)
    for chunk in stream:
        window.stream_text(chunk['message']['content'])
    root.mainloop()


def on_f8():
    print("f8 was pressed")
    fix_selection()

def on_f7():
    print("f7 was pressed")
    show_translation_in_ui()



if __name__ == "__main__":
    with keyboard.GlobalHotKeys({
        f"{f8}": on_f8,
        f"{f7}": on_f7}) as h:
     h.join()