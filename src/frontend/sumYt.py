# Extracts subtitles from Youtube Transcript API and sends them to text-davinci-003 for summariztion. Returns the output in the text area.

import re
import time
import tkinter as tk
from tkinter import Toplevel
from tkinter import filedialog #File System Access
import customtkinter #GUI Library
from customtkinter.windows.ctk_toplevel import CTkToplevel
from config.definitions import LOGOIMG
from youtube_transcript_api import YouTubeTranscriptApi

from PIL import Image, ImageTk #Image Processing

#Page Imports
import src.backend.formatter as formatter
import src.backend.openai as openai


class CustomToplevel(CTkToplevel):
    def __init__(self, dayOfMonth, time, dayOfWeek, month, title, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.title("Youtube Summarizer")

        #Getting Summary Data from homePage
        self.dayOfMonth = dayOfMonth
        self.time = time
        self.dayOfWeek = dayOfWeek
        self.month = month
        self.sumTitle = title
        self.summary = ""

        #GUI Elements

        #Main Page Logo
        self.mainlogo = customtkinter.CTkImage(
            light_image=Image.open(LOGOIMG),
            size=(90, 90)
        )
        self.logoBtn = customtkinter.CTkButton(
            self, 
            text="", 
            command=self.destroy,
            fg_color="transparent",
            image=self.mainlogo,
            state="disabled",
        )
        self.logoBtn.place(relx=0.065, rely=0.090, anchor=tk.CENTER)


        #Title Label
        self.title = customtkinter.CTkLabel(
            self,
            text="S Y N O P S I Z E",
            width=120,
            height=25,
            font=("Montserrat SemiBold", 34),
        )
        self.title.place(relx=0.50, rely=0.09, anchor=tk.CENTER)


        #YT Link Box
        self.linkBox = customtkinter.CTkEntry(
        self,
        placeholder_text="Enter your Link Here",
        width=500,
        height=65,
        font=("Montserrat SemiBold", 22),
        border_width=2,
        corner_radius=20,
        )
        self.linkBox.place(relx=0.5, rely=0.3, anchor=tk.CENTER)


        #Summary Title
        self.summarybox = customtkinter.CTkTextbox(
            self,
            width=600,
            height=200,
            font=("Montserrat SemiBold", 20),
            border_width=2,
            corner_radius=20,
            wrap="word"
        )
        self.summarybox.place(relx=0.5, rely=0.575, anchor=tk.CENTER)


        # Summarise using Text
        self.sumTextBtn = customtkinter.CTkButton(
            self, 
            text="Summarise",
            command=self.loadingSet,
            font=("Montserrat SemiBold", 30),
            width=190,
            height=65,
            corner_radius=50
        )
        self.sumTextBtn.place(relx=0.35, rely=0.85, anchor=tk.CENTER)


        # Download Summary
        self.downloadBtn = customtkinter.CTkButton(
            self, 
            text="Download Summary",
            command=self.downloadSummary,
            font=("Montserrat SemiBold", 26),
            width=190,
            height=65,
            corner_radius=50,
            state="disabled",
        )
        self.downloadBtn.place(relx=0.65, rely=0.85, anchor=tk.CENTER)

        # Exit button
        exitButton = customtkinter.CTkButton(
            self, 
            text="X", 
            hover_color="red",
            command=self.destroy,
            font=("Montserrat SemiBold", 30),
            width=30,
            height=30,
            corner_radius=50
        )
        exitButton.place(relx=0.935, rely=0.08, anchor=tk.CENTER)
    
    def combobox_callback(self, choice):
        """"Displays selected option in GUI"""
        print("ComCTkComboBox dropdown clicked:", choice)

    def loadingSet(self):
        self.summarybox.delete("0.0","end")
        self.summarybox.insert("0.0", "Loading...")
        self.after(1, self.convertToText)
            
    def convertToText(self):
        """"Reads text file and stores it. Then uses OpenAI's text model to generate its summary."""

        url = self.linkBox.get()

        # Check if the URL is a valid YouTube link
        ytRE = (
            r'(https?://)?(www\.)?'
            '(youtube|youtu|youtube-nocookie)\.(com|be)/'
            '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
        ytMatch = re.match(ytRE, url)

        if len(url) <= 0:
            self.summarybox.delete("0.0","end")
            self.summarybox.insert("0.0", "Please provide a link!")
            return
        elif not ytMatch:
            self.summarybox.delete("0.0","end")
            self.summarybox.insert("0.0", "Invalid Link, Please provide a valid Youtube Link!")
            return


        videoID = url.split("v=")
        srt = YouTubeTranscriptApi.get_transcript(videoID[1])
        print(len(srt))
        result = ''
        c = 0
        for item in srt:
            c += 1
            result += item['text']
            if c == 150:
                self.summary += openai.summarise(result)
                time.sleep(4)
                c = 0
                result = ''
        
        self.summary += openai.summarise(result)

        if result:
            self.summarybox.delete("0.0", "end")
            self.summarybox.insert("0.0", self.summary)
            self.downloadBtn.configure(state="normal")

    def downloadSummary(self):
        """Passes summary as well as other user inputs to wordDoc formatter as well as saves the file in .docx"""
        formatter.wordDoc(self.dayOfMonth, self.time, self.dayOfWeek, self.month, self.sumTitle, self.summarybox.get("0.0", "end"))