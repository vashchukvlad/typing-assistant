import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox


def save_to_db(text):
    # Replace with your actual DB saving logic
    print("Saving to DB...")
    print(text)
    messagebox.showinfo("Saved", "Text saved to database!")
    

class TextStreamWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Stream Viewer")
        self.root.geometry("700x500")
        self.root.configure(bg="#f5f5f5")  # Light background for Ubuntu look

        self.text_area = scrolledtext.ScrolledText(
            root,
            wrap=tk.WORD,
            font=("Ubuntu", 12),
            bg="white",
            fg="black",
            insertbackground="black",  # Cursor color
            borderwidth=2,
            relief="sunken"
        )
        self.text_area.pack(expand=True, fill="both", padx=10, pady=10)

        button_frame = tk.Frame(root, bg="#f5f5f5")
        button_frame.pack(pady=10)

        self.save_button = tk.Button(
            button_frame,
            text="💾 Save to DB and Close",
            command=self.save_and_close,
            bg="#4CAF50",
            fg="white",
            font=("Ubuntu", 11, "bold"),
            padx=10,
            pady=5
        )
        self.save_button.pack(side="left", padx=10)

        self.close_button = tk.Button(
            button_frame,
            text="❌ Close",
            command=self.close,
            bg="#f44336",
            fg="white",
            font=("Ubuntu", 11, "bold"),
            padx=10,
            pady=5
        )
        self.close_button.pack(side="left", padx=10)

    def save_and_close(self):
        text = self.text_area.get("1.0", tk.END).strip()
        if text:
            save_to_db(text)
        self.root.destroy()

    def close(self):
        self.root.destroy()

    def stream_text(self, new_text):
        self.text_area.insert(tk.END, new_text)
        self.text_area.see(tk.END)  # Auto-scroll