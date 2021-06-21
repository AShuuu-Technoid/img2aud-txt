# from typing_extensions import Required
import requests
import easyocr
import pyttsx3
import os
from art import *

class txtaud:
    def urldowntxt(self,urldowntxt):
        url = urldowntxt
        self.downfile=(url.rsplit('/', 1)[1])
        # print(url)
        response=requests.get(url)
        file = open(self.downfile,"wb")
        file.write(response.content)
        file.close()
        engine = pyttsx3.init()
        engine.setProperty("rate", 175)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[5].id)
        engine.say("Please wait while reading text")
        engine.runAndWait()
        reader=easyocr.Reader(['en'])
        results=reader.readtext(self.downfile)
        text=''
        for result in results:
            text +=result[1] + ' '
        # print(text)
        filname=(self.downfile.rsplit('.',1)[0])
        slcfile=(f"{filname}.txt")
        file1 = open(slcfile,"w")
        file1.write(text)
        engine.say(f"Image to text file saved as {slcfile}")
        engine.runAndWait()
        # self.out=(text)
    def urldown(self,urldown):
        url = urldown
        self.downfile=(url.rsplit('/', 1)[1])
        # print(url)
        response=requests.get(url)
        file = open(self.downfile,"wb")
        file.write(response.content)
        file.close()
        engine = pyttsx3.init()
        engine.setProperty("rate", 175)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[5].id)
        engine.say("Please wait while reading text")
        engine.runAndWait()
        reader=easyocr.Reader(['en'])
        results=reader.readtext(self.downfile)
        text=''
        for result in results:
            text +=result[1] + ' '
        self.out=(text)
    def spch(self):
        engine = pyttsx3.init()
        engine.setProperty("rate", 175)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[5].id)
        engine.say(self.out)
        engine.runAndWait()
    def aud_path(self):
        fpath= input("Enter Path with filename : ")
        engine = pyttsx3.init()
        engine.setProperty("rate", 175)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[5].id)
        engine.say("Please wait while reading text")
        engine.runAndWait()
        reader=easyocr.Reader(['en'])
        results=reader.readtext(fpath)
        text=''
        for result in results:
            text +=result[1] + ' '
        self.out=(text)
    def txt_path(self):
        fpath= input("Enter Path with filename : ")
        engine = pyttsx3.init()
        engine.setProperty("rate", 175)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[5].id)
        engine.say("Please wait while reading text")
        engine.runAndWait()
        reader=easyocr.Reader(['en'])
        results=reader.readtext(fpath)
        text=''
        for result in results:
            text +=result[1] + ' '
        filename=(fpath.rsplit('/',1)[1])
        filname=(filename.rsplit('.',1)[0])
        slcfile=(f"{filname}.txt")
        file1 = open(slcfile,"w")
        file1.write(text)
        engine.say(f"Image to text file saved as {slcfile}")
        engine.runAndWait()
    def rm(self):
        rmfile = os.getcwd() +"/"+self.downfile
        os.remove(rmfile)
    def txt(self):
        tprint("Img 2 Txt")
        res=input(f"1. Image from URL\n2. Image path\n\nSelect: ")
        if res == '1':
            urlink=input("Enter URL : ")
            s=txtaud()
            s.urldowntxt(urlink)
            s.rm()
        if res == '2':
            s=txtaud()
            s.txt_path()
    def aud(self):
        tprint("Img 2 Audio")
        res=input(f"1. Image from URL\n2. Image path\n\nSelect: ")
        if res == '1':
            urlink= input("Enter URL : ")
            s=txtaud()
            s.urldown(urlink)
            s.spch()
            s.rm()
        if res == '2':
            s=txtaud()
            s.aud_path()
            s.spch()
    def mainput(self):
        tprint("Welcome")
        res=input(f"1. Image to Audio\n2. Image To Text\n\nSelect: ")
        if res == '1':
            s.aud()
        if res == '2':
            s.txt()
if __name__ == "__main__":
    try:
        s=txtaud()
        s.mainput()
    except KeyboardInterrupt:
        print("\nProgram aborting due to control-C.\n")
        engine = pyttsx3.init()
        engine.setProperty("rate", 175)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[5].id)
        engine.say("Program aborting due to control-C.")
        engine.runAndWait()
