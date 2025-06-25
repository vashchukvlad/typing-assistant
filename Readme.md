# 📝 Text Fixer Hotkey Tool

This is a simple Python tool that listens for the **F8** key globally and automatically fixes typos, punctuation, and casing in the selected text using an [Ollama](https://ollama.com) language model. The corrected text is placed back into your clipboard and pasted automatically.

---

## ✨ Features

- 🔤 Fixes typos, punctuation, and casing in any selected text. Triggered globally via the `F8` key.
- ⌨️ Translate text to Ukrainian language. Triggered globally via the `F7` key.
- 🧠 Uses a local Ollama language model (e.g., `Mistral`) for correction.
- 📋 Works with the system clipboard.
- ⚡ Real-time streaming response from the model.

---

## 🚀 How It Works

1. You select text in **any application**.
2. You press **F8**.
3. The program:
   - Copies the selected text.
   - Sends it to a local LLM via `ollama`.
   - Replaces the original text with the corrected version.

---

## 🛠️ Requirements

- Python 3.7+
- A running [Ollama](https://ollama.com/) server with a model like `mistral` installed.

### 📦 Python Dependencies

Install with `pip`:

```bash
pip install -r requirements.txt

python main.py
