from tkinter import *
import os
from tkinter import ttk,filedialog
from pygame import mixer
import tkinter as tk
from PIL import Image,ImageTk


root=Tk()

root.title("Music Player")
root.geometry("920x670+290+85")
root.configure(bg="#0f1a2b")
root.resizable(False,False)

mixer.init()

def my_song():
    path=filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END,song)

def play_song():
    music_name=playlist.get(ACTIVE)
    #print(music_name[0:2])
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text=music_name[0:])

#icon
image_icon=PhotoImage(file="logo.png")
root.iconphoto(False,image_icon)

top=PhotoImage(file="top.png")
Label(root,image=top,bg="#0f1a2b").pack()

#logo
Logo=PhotoImage(file="logo.png")
Label(root,image=Logo,bg="#0f1a2b").place(x=65,y=115)

#Button 
play_btn=PhotoImage(file="play.png")
Button(root,image=play_btn,bg="black",bd=0,command=play_song).place(x=100,y=400)

stop_btn=PhotoImage(file="stop.png")
Button(root,image=stop_btn,bg="black",bd=0,command=mixer.music.stop).place(x=30,y=540)

resume_btn=PhotoImage(file="resume.png")
Button(root,image=resume_btn,bg="black",bd=0,command=mixer.music.unpause).place(x=120,y=540)

pause_btn=PhotoImage(file="pause.png")
Button(root,image=pause_btn,bg="black",bd=0,command=mixer.music.pause).place(x=210,y=540)

#Label
music=Label(root,text="",font=("arial",15),fg='white',bg="#0f1a2b")
music.place(x=150,y=340,anchor='center')


#music

Meenu=PhotoImage(file="menu.png")
Label(root,image=Meenu,bg="#0f1a2b").pack(padx=10,pady=50,side='right')

music_frame=Frame(root,bd=2,relief='ridge')
music_frame.place(x=330,y=350,width=560,height=250)

Button(root,text="Open Folder",font=("arial",10,"bold"),fg='white',bg='blue',command=my_song).place(x=330,y=300)

scroll=Scrollbar(music_frame)
playlist=Listbox(music_frame,width=100,font=("arial",10,"bold"),fg="grey",bg="#333333",selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side='right',fill=Y)
playlist.pack(side='left',fill=BOTH)

root.mainloop()