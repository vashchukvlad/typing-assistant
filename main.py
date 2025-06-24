import time

from pynput import keyboard
import pyperclip
import ollama

from prompts import FIX_TYPOS_PROMPT


def fix_text(text):
    # prompt = FIX_TYPOS_PROMPT.substitute(text=text)
    # response = ollama.chat(model='mistral:7b-instruct-v0.2-q4_K_S', messages=[
    # {
    #     'role': 'user',
    #     'content': prompt,
    #     'keep_alive': "5m"
    # },
    # ])

    # return response['message']['content']

    from ollama import chat

    prompt = FIX_TYPOS_PROMPT.substitute(text=text)
    stream = chat(
        model='mistral:7b-instruct-v0.2-q4_K_S',
        messages=[
        {
            'role': 'user',
            'content': prompt,
            'keep_alive': "5m"
        }],
        stream=True,
    )

    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)



controller = keyboard.Controller()

f9 = keyboard.Key.f9.value
f8 = keyboard.Key.f8.value


def fix_current_line():
    controller.press(keyboard.Key.ctrl)
    controller.press(keyboard.Key.shift)
    controller.press(keyboard.Key.left)

    controller.release(keyboard.Key.ctrl)
    controller.release(keyboard.Key.shift)
    controller.release(keyboard.Key.left)

    fix_selection()


def fix_selection():
    with controller.pressed(keyboard.Key.ctrl):
        controller.tap('c')

    time.sleep(0.1)
    text = pyperclip.paste()
    print(text)

    fixed_text = fix_text(text)

    pyperclip.copy(fixed_text)
    time.sleep(0.1)

    with controller.pressed(keyboard.Key.ctrl):
        controller.tap('v')


def on_f9():
    fix_current_line()


def on_f8():
    print("f8 was pressed")
    #fix_selection()


with keyboard.GlobalHotKeys({
        f"{f9}": on_f9,
        f"{f8}": on_f8}) as h:
    h.join()
