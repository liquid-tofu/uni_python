import sys
import pytesseract
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
from deep_translator import GoogleTranslator


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

title_font = ("arial", 12)

# init
root = tk.Tk()
root.geometry("600x500")
root.config(padx=10, pady=10)

# for scaling size
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)

# title of the app
tlabel = tk.Label(root, text="|", font=title_font)
tlabel.grid(columnspan=2, row=0, column=0, pady=(0, 10))

# screen for displaying image
left_frame = tk.Frame(root, width=285, height=150, padx=5, pady=5,
                      highlightthickness=1,
                      highlightbackground="green")
left_frame.grid(column=0, row=1, padx=(0, 3), sticky="nsew")
left_frame.grid_propagate(False)
left_frame.rowconfigure(0, weight=1)
left_frame.columnconfigure(0, weight=1)

img_screen = tk.Canvas(left_frame)
img_screen.grid(row=0, column=0, sticky="nsew")

# screen for displaying text
right_frame = tk.Frame(root, width=285, height=150)
right_frame.grid(column=1, row=1, padx=(3, 0), sticky="nsew")
right_frame.grid_propagate(False)
right_frame.rowconfigure(0, weight=1)
right_frame.columnconfigure(0, weight=1)

txt_screen = tk.Text(right_frame, padx=5, pady=5, state="disabled")
txt_screen.grid(row=0, column=0, sticky="nsew")




txt_screen.config(state="normal")
txt_screen.insert("end", "")
txt_screen.config(state="disabled")

root.mainloop()


"""
def select_file():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)

    file_path = filedialog.askopenfilename(
        title="Select a file",
        initialdir="D:/",
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ico")]
    )
    root.destroy()
    return file_path

def extract_text(image):
    try:
        text = pytesseract.image_to_string(image, lang="khm+chi_sim+eng+rus").strip()
        if text:
            translated = GoogleTranslator(source='auto', target='en').translate(text)

            print("\n### Extracted Text ###\n")
            print(f"@@@ Original: {text}\n")
            print(f"@@@ Translated: {translated}\n")
            return
        else:
            print("\nCannot detect!\n")
            return
    except Exception as e:
        print(f"\nError: {e}\n")
        return

while True:
    cmd = input("s > select, f > fill, x > exit\n"
                "Option: ")
    if cmd.lower() == "x":
        print("Exiting...")
        sys.exit()
    elif cmd.lower() == "s":
        file_image = select_file()
    elif cmd.lower() == "f":
        file_image = input("Enter filename: ")
    else:
        print("Error: invalid command!\n")
        continue

    if not file_image:
        print("\nBruh you're not selecting anything!\n")
        continue

    try:
        image = Image.open(file_image)
    except Exception as e:
        print(f"\nError: {e}\n")
        continue

    extract_text(image)
"""

