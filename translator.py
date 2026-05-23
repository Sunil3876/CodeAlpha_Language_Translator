import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

class ModernTranslator:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Language Translator Pro")
        self.root.geometry("750x550")
        self.root.configure(bg="#1e1e2e")  # Modern Deep Slate/Dark Background
        self.root.resizable(False, False)

        # Style Configuration for generic system layouts
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Comprehensive Supported Languages List
        self.languages = {
            "Hindi": "hi", "English": "en", "French": "fr", "Spanish": "es",
            "German": "de", "Japanese": "ja", "Arabic": "ar", "Russian": "ru",
            "Italian": "it", "Korean": "ko"
        }

        self.create_widgets()

    def create_widgets(self):
        # 1. Header Banner
        title_frame = tk.Frame(self.root, bg="#252538", height=70)
        title_frame.pack(fill="x", side="top")
        title_frame.pack_propagate(False)

        title_label = tk.Label(
            title_frame, text="🌍 AI MULTI-LANGUAGE TRANSLATOR", 
            font=("Segoe UI", 15, "bold"), fg="#89b4fa", bg="#252538"
        )
        title_label.pack(pady=18)

        # Main Content Wrapper
        main_frame = tk.Frame(self.root, bg="#1e1e2e")
        main_frame.pack(fill="both", expand=True, padx=30, pady=20)

        # 2. Input Layout Component
        lbl_input = tk.Label(main_frame, text="Enter Source Text (English):", font=("Segoe UI", 11, "bold"), fg="#cdd6f4", bg="#1e1e2e")
        lbl_input.pack(anchor="w", pady=(0, 5))

        self.src_text = tk.Text(
            main_frame, font=("Segoe UI", 11), bg="#2d2d44", fg="#f8f8f2", 
            wrap="word", bd=0, highlightthickness=1, highlightbackground="#444464", highlightcolor="#89b4fa"
        )
        self.src_text.pack(fill="x", height=110, pady=(0, 15))
        self.src_text.insert("1.0", "Type your text here...")
        self.src_text.bind("<FocusIn>", self.clear_placeholder)

        # 3. Control Center Panel (Dropdown & Button Execution)
        control_frame = tk.Frame(main_frame, bg="#1e1e2e")
        control_frame.pack(fill="x", pady=(0, 15))

        lbl_lang = tk.Label(control_frame, text="Target Language:", font=("Segoe UI", 11, "bold"), fg="#cdd6f4", bg="#1e1e2e")
        lbl_lang.pack(side="left", padx=(0, 10))

        # Styling Combo Box Options
        self.style.configure("TCombobox", fieldbackground="#2d2d44", background="#2d2d44", foreground="#f8f8f2", arrowcolor="#89b4fa")
        self.lang_box = ttk.Combobox(control_frame, values=list(self.languages.keys()), state="readonly", font=("Segoe UI", 10), width=22)
        self.lang_box.set("Hindi")
        self.lang_box.pack(side="left")

        # Flat Modern Design CTA Button
        self.btn_translate = tk.Button(
            control_frame, text="Translate Now ✨", font=("Segoe UI", 11, "bold"),
            bg="#1e66f5", fg="#ffffff", activebackground="#004fc4", activeforeground="#ffffff",
            bd=0, cursor="hand2", padx=25, pady=6, command=self.translate_text
        )
        self.btn_translate.pack(side="right")

        # 4. Output Layout Component
        lbl_output = tk.Label(main_frame, text="Translated Output:", font=("Segoe UI", 11, "bold"), fg="#cdd6f4", bg="#1e1e2e")
        lbl_output.pack(anchor="w", pady=(0, 5))

        self.dest_text = tk.Text(
            main_frame, font=("Segoe UI", 11), bg="#2d2d44", fg="#a6e3a1", 
            wrap="word", bd=0, highlightthickness=1, highlightbackground="#444464", state="disabled"
        )
        self.dest_text.pack(fill="both", expand=True)

    def clear_placeholder(self, event):
        if self.src_text.get("1.0", "end-1c") == "Type your text here...":
            self.src_text.delete("1.0", "end")

    def translate_text(self):
        text_to_translate = self.src_text.get("1.0", "end-1c").strip()
        if not text_to_translate or text_to_translate == "Type your text here...":
            messagebox.showwarning("Input Error", "Please enter some text to process.")
            return

        target_lang_name = self.lang_box.get()
        target_lang_code = self.languages.get(target_lang_name)

        try:
            self.btn_translate.config(text="Processing Async...", state="disabled")
            self.root.update_idletasks()

            # Dynamic Core Pipeline Integration
            translated = GoogleTranslator(source='auto', target=target_lang_code).translate(text_to_translate)
            
            self.dest_text.config(state="normal")
            self.dest_text.delete("1.0", "end")
            self.dest_text.insert("1.0", translated)
            self.dest_text.config(state="disabled")
        except Exception as e:
            messagebox.showerror("Network Matrix Error", f"Failed to connect to the pipeline endpoint.\nDetails: {str(e)}")
        finally:
            self.btn_translate.config(text="Translate Now ✨", state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernTranslator(root)
    root.mainloop()