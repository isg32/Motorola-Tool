import tkinter as tk
from tkinter import scrolledtext, filedialog
import sys
import subprocess
from zipfile import ZipFile
import customtkinter

class MotorolaToolApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # System Settings
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("blue")

        # Create the main window
        self.geometry("720x640")
        self.title("Motorola-Tool")

        # Ui Elements
        self.title_label = customtkinter.CTkLabel(self, text="Motorola-Tool", font=("Helvetica", 16))
        self.title_label.pack(padx=10, pady=10)

        self.info_label1 = customtkinter.CTkLabel(self, text="Notes \n\n1. Make Sure To Add the rom first \n2. Only Use Rom Files from Lolinet or RSA \n3. Don't Panic, the zip extraction may look like a frozen system")
        self.info_label1.pack(pady=10)

        # Button to trigger zip extraction
        self.extract_button = customtkinter.CTkButton(self, text="Extract Zip", command=self.extract_zip)
        self.extract_button.pack(pady=10)

        # Button to run runhanoip
        self.run_button = customtkinter.CTkButton(self, text="Begin Install", command=self.runhanoip)
        self.run_button.pack(pady=10)

        # Console-like output using ScrolledText
        self.console_output = scrolledtext.ScrolledText(self, height=30, width=90, wrap=tk.WORD, bg='white', fg='black')
        self.console_output.pack(padx=10, pady=10)

        # Function to redirect stdout to the console_output ScrolledText widget
        sys.stdout.write = lambda s: self.console_output.insert(tk.END, s)

    def runhanoip(self):
        process = subprocess.Popen("cd system && test hanoip && cd ..", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            while True:
                output = process.stdout.readline().decode('utf-8')
                if not output:
                    break
                self.console_output.insert(tk.END, output)
                self.console_output.see(tk.END)  # Scroll to the bottom
        except subprocess.CalledProcessError as e:
            self.console_output.insert(tk.END, f"Error: {e}\n")
        finally:
            process.terminate()

    def extract_zip(self):
        zip_path = filedialog.askopenfilename(title="Select a Zip File", filetypes=[("Zip files", "*.zip")])

        if zip_path:
            extract_path = "./system"

            with ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)
            self.console_output.insert(tk.END, f"Extracted {zip_path} to {extract_path}\n")
            self.console_output.see(tk.END)  # Scroll to the bottom

if __name__ == "__main__":
    app = MotorolaToolApp()
    app.mainloop()
