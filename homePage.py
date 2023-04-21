import tkinter as tk
import customtkinter #GUI Library
from customtkinter.windows.ctk_toplevel import CTkToplevel
from PIL import Image, ImageTk #Image Processing
from config.definitions import LOGOIMG

import sumAudio #Page Import
import sumText #Page Import
import creditsPage #PageImport

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("900x600")
app.title("AI Inside ;)")


def showAudioPage():
    """"Displays a Top Level page of Summary Audio Page"""
    custom_toplevel = sumAudio.CustomToplevel(dayOfMonthBox.get(), dayOfWeekBox.get(), timeBox.get(), monthBox.get(), str(titleBox.get()))
    custom_toplevel.geometry("900x600")
    custom_toplevel.mainloop()

def showTextPage():
    """"Displays a Top Level page of Audio Page"""
    custom_toplevel = sumText.CustomToplevel(dayOfMonthBox.get(), dayOfWeekBox.get(), timeBox.get(), monthBox.get(), str(titleBox.get()))
    custom_toplevel.geometry("900x600")
    custom_toplevel.mainloop()

def showCreditsPage():
    """"Displays a Top Level page of CreditsPage"""
    custom_toplevel = creditsPage.CustomToplevel()
    custom_toplevel.geometry("400x400")
    custom_toplevel.mainloop()

def combobox_callback(choice):
    """"Displays selected option in GUI"""
    print("ComCTkComboBox dropdown clicked:", choice)


#GUI Elements


#Main Page Logo
mainlogo = customtkinter.CTkImage(
    light_image=Image.open(LOGOIMG),
    size=(90, 90)
)
logoBtn = customtkinter.CTkButton(
    master=app, 
    text="", 
    fg_color="transparent",
    image=mainlogo,
    state="disabled",
)
logoBtn.place(relx=0.065, rely=0.090, anchor=tk.CENTER)


#Title Label
label = customtkinter.CTkLabel(
    master=app,
    text="S Y N O P S I Z E",
    width=120,
    height=25,
    font=("Montserrat SemiBold", 34),)
label.place(relx=0.50, rely=0.09, anchor=tk.CENTER)


#Info and Credits Button
creditsBtn = customtkinter.CTkButton(
    master=app, 
    text="i", 
    command=showCreditsPage,
    font=("Montserrat SemiBold", 30),
    width=60,
    height=60,
    corner_radius=20,
    border_color="gray",
    fg_color="transparent",
    text_color=("black","white"),
    border_width=3
)
creditsBtn.place(relx=0.935, rely=0.08, anchor=tk.CENTER)


#Day of Month Options
dayOfMonth = ["Day of Month"]

for i in range(1, 32):
    if(i == 1 or i == 21 or i == 31):
        dayOfMonth.append(str(i) + "st")
    elif(i == 2 or i == 22):
        dayOfMonth.append(str(i) + "nd")
    elif(i == 3 or i == 23):
        dayOfMonth.append(str(i) + "rd")
    else:
        dayOfMonth.append(str(i) + "th")


dayOfMonthBox = customtkinter.CTkComboBox(
    master=app,
    values=dayOfMonth,
    command=combobox_callback,
    variable=customtkinter.StringVar(value=dayOfMonth[0]),  # Set Initial Value
    width=250,
    height=60,
    font=("Montserrat SemiBold", 20),
    corner_radius=20
)
dayOfMonthBox.place(relx=0.35, rely=0.225, anchor=tk.CENTER)


#Month Options
month = ["Month", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


monthBox = customtkinter.CTkComboBox(
    master=app,
    values=month,
    command=combobox_callback,
    variable=customtkinter.StringVar(value=month[0]),  # Set initial value
    width=250,
    height=60,
    font=("Montserrat SemiBold", 20),
    corner_radius=20
)
monthBox.place(relx=0.65, rely=0.225, anchor=tk.CENTER)


#Day of Week Options
dayofWeek = ['Day','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


dayOfWeekBox = customtkinter.CTkComboBox(
    master=app,
    values=dayofWeek,
    command=combobox_callback,
    variable=customtkinter.StringVar(value=dayofWeek[0]),  # set initial value
    width=250,
    height=60,
    font=("Montserrat SemiBold", 20),
    corner_radius=20
)
dayOfWeekBox.place(relx=0.35, rely=0.375, anchor=tk.CENTER)


#Time of Day Options
timeOfDay = ['Time']

for hour in range(0, 24):
    for minute in ['00', '30']:
        time = f'{hour:02d}:{minute} hrs'
        timeOfDay.append(time)


timeBox = customtkinter.CTkComboBox(
    master=app,
    values=timeOfDay,
    command=combobox_callback,
    variable=customtkinter.StringVar(value=timeOfDay[0]),  # set initial value
    width=250,
    height=60,
    font=("Montserrat SemiBold", 20),
    corner_radius=20
)
timeBox.place(relx=0.65, rely=0.375, anchor=tk.CENTER)


#Summary Title
titleBox = customtkinter.CTkEntry(
    master=app,
    placeholder_text="Your title here.",
    width=520,
    height=60,
    font=("Montserrat SemiBold", 20),
    border_width=2,
    corner_radius=20,
)
titleBox.place(relx=0.5, rely=0.525, anchor=tk.CENTER)


# Summarise using Audio
sumAudioBtn = customtkinter.CTkButton(
    master=app, 
    text="Summarise using Audio",
    command=showAudioPage,
    font=("Montserrat SemiBold", 30),
    width=190,
    height=65,
    corner_radius=50
)
sumAudioBtn.place(relx=0.5, rely=0.70, anchor=tk.CENTER)

# Summarise using Text
sumTextBtn = customtkinter.CTkButton(
    master=app, 
    text="Summarise using Text", 
    command=showTextPage,
    font=("Montserrat SemiBold", 30),
    width=190,
    height=65,
    corner_radius=50
)
sumTextBtn.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

# Exit button
exitButton = customtkinter.CTkButton(
    master=app, 
    text="X", 
    hover_color="red",
    command=app.destroy,
    font=("Montserrat SemiBold", 30),
    width=30,
    height=30,
    corner_radius=50
)
exitButton.place(relx=0.925, rely=0.925, anchor=tk.CENTER)

app.mainloop()

