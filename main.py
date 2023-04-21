import tkinter as tk
import customtkinter #GUI Library
from PIL import Image, ImageTk
from itertools import count, cycle
import subprocess
from config.definitions import SPLASH_SCREEN

class ImageLabel(tk.Label):
    """
    A Label that displays images, and plays them if they are gifs
    :im: A PIL Image instance or a string filename
    """
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)

app = customtkinter.CTk()
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
app.geometry("900x600")
app.title("Synopsize")

#Title Label
label = customtkinter.CTkLabel(
    master=app,
    text="S Y N O P S I Z E",
    width=120,
    height=25,
    font=("Montserrat SemiBold", 34),)

label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

lbl = ImageLabel(app)
lbl.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
app.update()
lbl.load(SPLASH_SCREEN)

# Start the second script after 4000 seconds
app.after(4000, lambda: start_second_script(app))

def start_second_script(app):
    subprocess.Popen(['python3', 'homePage.py'])
    app.quit()

app.mainloop()
