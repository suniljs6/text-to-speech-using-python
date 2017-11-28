# Import the required module for text 
# to speech conversion

from gtts import gTTS
import tkinter
from tkinter import *

root = Tk()
root.title('T-T-S')
Label(text='TEXT TO SPEECH').pack(side=TOP,padx=50,pady=50)

mytext = Entry(root, width=10)
mytext.pack(side=TOP,padx=10,pady=10)




import os
#mytext = 'Good morning devil'
language = 'en'
def onok():
        a=mytext.get();
	myobj = gTTS(text=a, lang=language, slow=False)
        myobj.save("welcome.mp3")
        os.system("totem welcome.mp3")



Button(root, text='CONVERT', command=onok).pack(side=LEFT)


root.mainloop()

