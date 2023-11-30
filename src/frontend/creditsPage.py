# A little about the App and links of the Developers Social Profiles.

import tkinter as tk
from tkinter import Toplevel
from tkinter import filedialog #File System Access
import customtkinter #GUI Library
from customtkinter.windows.ctk_toplevel import CTkToplevel
from config.definitions import LOGOIMG
import webbrowser

class CustomToplevel(CTkToplevel):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.title("The Devs.")

        #GUI Elements

        #Thank You Message
        self.userMessage = customtkinter.CTkTextbox(
            self,
            width=350,
            height=200,
            font=("Montserrat SemiBold", 19),
            fg_color="transparent",
            corner_radius=20,
            wrap="word"
        )
        self.userMessage.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        self.userMessage.insert("0.0", "Hey User! hope you find Synopsize useful. It was developed during our Engg. Sem IV and learned a lot while building it. If you would like to give feedback or connect with us, click on a link below.     - Abhi")

        #DevLinks
        self.abhi = customtkinter.CTkButton(
            self, 
            text="Abhi", 
            command= lambda: self.open_link("abhi"),
            font=("Montserrat SemiBold", 20),
            width=60,
            fg_color="transparent",
            text_color=("black","white"),
        )
        self.abhi.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        self.altaf = customtkinter.CTkButton(
            self, 
            text="Altaf", 
            command= lambda: self.open_link("altaf"),
            font=("Montserrat SemiBold", 20),
            width=60,
            fg_color="transparent",
            text_color=("black","white"),
        )
        self.altaf.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        self.sarah = customtkinter.CTkButton(
            self, 
            text="Sarah", 
            command= lambda: self.open_link("sarah"),
            font=("Montserrat SemiBold", 20),
            width=60,
            fg_color="transparent",
            text_color=("black","white"),
        )
        self.sarah.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

        self.amisha = customtkinter.CTkButton(
            self, 
            text="Amisha", 
            command= lambda: self.open_link("amisha"),
            font=("Montserrat SemiBold", 20),
            width=60,
            fg_color="transparent",
            text_color=("black","white"),
        )
        self.amisha.place(relx=0.5, rely=0.9, anchor=tk.CENTER)


    def open_link(self,head):
        if(head == "abhi"):
            webbrowser.open_new("https://linktr.ee/abhigyanbafna")
        elif(head == "altaf"):
            webbrowser.open_new("https://twitter.com/Altaf0032")
        elif(head == "sarah"):
            webbrowser.open_new("https://twitter.com/5arahkhan")
        elif(head == "amisha"):
            webbrowser.open_new("https://twitter.com/AmishaShahi4")