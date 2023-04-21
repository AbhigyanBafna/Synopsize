import tkinter as tk
from tkinter import Toplevel
from tkinter import filedialog #File System Access
import customtkinter #GUI Library
from customtkinter.windows.ctk_toplevel import CTkToplevel
from config.definitions import LOGOIMG, ROOT_DIR

from PIL import Image, ImageTk #Image Processing

from pydub import AudioSegment #Audio Processing
from pydub.utils import make_chunks
import speech_recognition as sr
from tkinter import messagebox

import pyaudio #Live Recording
import wave
import io

#Page Imports
import formatter
import openai


class CustomToplevel(CTkToplevel):
    def __init__(self, dayOfMonth, time, dayOfWeek, month, title, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.title("Audio Summary")

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
            command=self.browseFile,
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


        # Browse Audio
        self.browseBtn = customtkinter.CTkButton(
            self, 
            text="Browse Audio File",
            command=self.browseFile,
            font=("Montserrat SemiBold", 30),
            width=200,
            height=65,
            corner_radius=50
        )
        self.browseBtn.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
            
        #RecordTime Box
        self.recBox = customtkinter.CTkEntry(
        self,
        placeholder_text="Record Time in Mins",
        width=230,
        height=65,
        font=("Montserrat SemiBold", 20),
        border_width=2,
        corner_radius=20,
        )
        self.recBox.place(relx=0.35, rely=0.45, anchor=tk.CENTER)


        # Live Rec
        self.liveBtn = customtkinter.CTkButton(
            self, 
            text="Record 🔴",
            command=self.liveRec,
            font=("Montserrat SemiBold", 30),
            width=240,
            height=65,
            corner_radius=50
        )
        self.liveBtn.place(relx=0.65, rely=0.45, anchor=tk.CENTER)


        #Summary Title
        self.summarybox = customtkinter.CTkTextbox(
            self,
            width=600,
            height=100,
            font=("Montserrat SemiBold", 20),
            border_width=2,
            corner_radius=20,
            wrap="word"
        )
        self.summarybox.place(relx=0.5, rely=0.65, anchor=tk.CENTER)


        # Summarise using Audio
        self.sumAudioBtn = customtkinter.CTkButton(
            self, 
            text="Summarise",
            command=self.loadingSet,
            font=("Montserrat SemiBold", 30),
            width=190,
            height=65,
            corner_radius=50
        )
        self.sumAudioBtn.place(relx=0.35, rely=0.85, anchor=tk.CENTER)


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

    def browseFile(self):
        """"Acepts Audio file from File System Browser"""
        self.filename = filedialog.askopenfilename(filetypes=(("mp3 File", "*.mp3"), ("wav File", "*.wav"), ("Audio Files", "*.*")))
        self.displayname = ".../" + self.filename.split("/")[-1][:15] + "..."
        if self.displayname:
            self.browseBtn.configure(text=self.displayname)

    def loadingSet(self):
        self.summarybox.insert("0.0", "Loading...")
        self.after(1, self.convertToText)

    def convertToText(self):
        """"Converts Audio to .wav format, converts it into text using Google's SpeechRecogniser. 
        Then uses OpenAI's text model to generate its summary."""
        audio_file = self.filename
        try:
            
            # Load the audio file using pydub
            sound = AudioSegment.from_file(audio_file)

            # Convert to WAV format
            raw_data = io.BytesIO(sound.raw_data)
            wav_data = io.BytesIO()
            sound.export(wav_data, format="wav")
            wav_data.seek(0)
            
            text = ''
            myaudio = AudioSegment.from_file(wav_data)
            chunks_length_ms = 180000
            chunks = make_chunks(myaudio, chunks_length_ms)
            for i, chunk in enumerate(chunks):
                chunkName = "./config/chunked/audioChunk" + f"{i}.wav"
                print("Exporting", chunkName)
                chunk.export(chunkName, format="wav")

                # Set up a SpeechRecognition recognizer instance
                r = sr.Recognizer()
                with sr.AudioFile(chunkName) as source:
                    audio = r.record(source)
                rec = r.recognize_google(audio, language="en-IN")
                text = "".join([text, rec])

            
            self.summary = openai.summarise(str(text))

        except Exception as e:
            print(e)

        if audio_file:
            self.summarybox.delete("0.0","end")
            self.summarybox.insert("0.0", self.summary)
            self.downloadBtn.configure(state="normal")

    def test(self):
        print(self.sumTitle)

    def liveRec(self):
        """"Opens Microphone and records audio for a minute. Saves the audio in the same directory named recording.wav"""
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        RECORD_SECONDS = round(float(self.recBox.get())*60)
        print(RECORD_SECONDS)
        WAVE_OUTPUT_FILENAME = "recording.wav"

        audio = pyaudio.PyAudio()

        # start recording
        messagebox.showinfo("Recoding started","Start recording...")
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                            rate=RATE, input=True,
                            frames_per_buffer=CHUNK)

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        # stop recording
        messagebox.showinfo("Recording ended","Recording Completed & Save Succesfully!")
        stream.stop_stream()
        stream.close()
        audio.terminate()

        # save the recording to a WAV file
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

        self.filename = ROOT_DIR + "/recording.wav"
        self.displayname = ".../" + self.filename.split("/")[-1][:15] + "..."
        if self.displayname:
            self.browseBtn.configure(text=self.displayname)



    def downloadSummary(self):
        """Passes summary as well as other user inputs to wordDoc formatter as well as saves the file in .docx"""
        formatter.wordDoc(self.dayOfMonth, self.time, self.dayOfWeek, self.month, self.sumTitle, self.summarybox.get("0.0", "end"))
        