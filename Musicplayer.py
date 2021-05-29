def mutemusic():
    global l
    l = mixer.music.get_volume()
    mixer.music.set_volume(0)
    root.MuteButton.grid_remove()
    root.UnMuteButton.grid()
    status.configure(text="Muted")
def unmutemusic():
    global l
    mixer.music.set_volume(l)
    root.MuteButton.grid()
    root.UnMuteButton.grid_remove()
    status.configure(text="Unmuted and playing....")

def pausemusic():
    mixer.music.pause()
    root.PauseButton.grid_remove()
    root.ResumeButton.grid()
    status.configure(text="Pause")

def resumemusic():

    root.ResumeButton.grid_remove()
    root.PauseButton.grid()
    mixer.music.unpause()
    status.configure(text="Resume and playing...")

def stopmusic():

    mixer.music.stop()
    ProgressMusic.ProgressStart.configure(text = "00:00:00")
    status.configure(text="Stopped")


def volumeupmusic():

    k = mixer.music.get_volume()
    mixer.music.set_volume(k+0.05)
    ProgressVolumeLabel.configure(text = "{}%".format(int(mixer.music.get_volume()*100)))
    ProgressVolume['value'] = mixer.music.get_volume()*100


def volumedownmusic():

    k = mixer.music.get_volume()
    mixer.music.set_volume(k - 0.05)
    ProgressVolumeLabel.configure(text="{}%".format(int(mixer.music.get_volume() * 100)))
    ProgressVolume['value'] = mixer.music.get_volume() * 100


def playmusic():

    k = audio.get()
    mixer.music.load(k)
    mixer.music.play()
    ProgressLabel.grid()
    ProgressMusic.grid()
    mixer.music.set_volume(0.5)
    ProgressVolumeLabel.configure(text="50%")
    ProgressVolume['value'] = 50
    root.MuteButton.grid()
    status.configure(text = "Playing........")

    song = MP3(k)
    totalcurrlen = int(song.info.length)
    ProgressMap['maximum'] = totalcurrlen
    ProgressEnd.configure(text = '{}'.format(datetime.timedelta(seconds=totalcurrlen)))
    def Progressbarmusic():
        currentsong = mixer.music.get_pos()//1000
        ProgressMap['value'] = currentsong
        ProgressMusic.ProgressStart.configure(text='{}'.format(datetime.timedelta(seconds=currentsong)))
        ProgressMap.after(2,Progressbarmusic)
    Progressbarmusic()

def musicurl():
        url = filedialog.askopenfilename(title = 'Select Music file',
                                         filetype = (("MP3","*.mp3"),("WAV","*.wav")))
        audio.set(url)






def createwidths():

    global search,play,pause,stop,volumeup,volumedown,resume,mute,unmute,status
    global ProgressLabel,ProgressVolume,ProgressVolumeLabel,ProgressMusic, ProgressMap,ProgressEnd,ProgressStart


    search = PhotoImage(file = "serach2.png")
    play = PhotoImage(file="play.png")
    pause = PhotoImage(file="pause.png")
    stop = PhotoImage(file="stop.png")
    resume = PhotoImage(file="play.png")
    volumeup = PhotoImage(file="volumeup.png")
    volumedown = PhotoImage(file="volumedown.png")
    mute = PhotoImage(file = "mute.png")
    unmute = PhotoImage(file = "unmute.png")

    search.subsample(2,2)
    play.subsample(2,2)
    pause.subsample(2, 2)
    stop.subsample(2, 2)
    volumeup.subsample(2, 2)
    volumedown.subsample(2, 2)
    resume.subsample(2,2)
    mute.subsample(2,2)
    unmute.subsample(2,2)







    TrackLabel = Label(root,text = "Select Audio : ", background = 'lightskyblue', font = ('arial', 15, 'italic bold'))
    TrackLabel.grid(row = 0, column = 1, padx = 20, pady = 20)

    status =Label(root,text = " ", background = 'DimGray',fg = "white", font = ('arial', 15, 'italic bold'))
    status.grid(row = 2, column = 2, padx = 20, pady = 20)

    TrackLabelEntry = Entry(root,font = ('arial', 16, 'italic bold'), textvariable = audio)
    TrackLabelEntry.grid(row = 0, column = 2, padx = 20, pady = 20)

    SearchButton = Button(root,text ="Search",background = 'white', font = ('arial', 13, 'italic bold'),width = 200, bd = 5,
                          image = search, compound = RIGHT, command = musicurl)
    SearchButton.grid(row = 0, column = 4, padx = 20, pady = 20)


    PlayButton = Button(root,text ="Play",background = 'orange', font = ('arial', 13, 'italic bold'),width = 200, bd = 5,
                        image = play, compound = RIGHT, command = playmusic)
    PlayButton.grid(row = 1, column = 1, padx = 20, pady = 20)

    root.PauseButton = Button(root,text ="Pause",background = 'orchid', font = ('arial', 13, 'italic bold'),width = 200, bd = 5,
                         image = pause, compound = RIGHT, command = pausemusic)
    root.PauseButton.grid(row = 1, column = 2, padx = 20, pady = 20)

    StopButton = Button(root,text ="Stop",background = 'cyan', font = ('arial', 13, 'italic bold'),width = 200, bd = 5,
                        image = stop, compound = RIGHT, command = stopmusic)
    StopButton.grid(row = 2, column = 1, padx = 20, pady = 20)


    VolumeupButton = Button(root,text ="Volumeup",background = 'khaki', font = ('arial', 13, 'italic bold'),width = 200, bd = 5,
                            image = volumeup, compound = RIGHT, command = volumeupmusic)
    VolumeupButton.grid(row = 1, column = 4, padx = 20, pady = 20)

    VolumedownButton = Button(root,text ="VolumeDown",background = 'khaki', font = ('arial', 13, 'italic bold'),width = 200, bd = 5,
                              image = volumedown, compound = RIGHT, command = volumedownmusic)
    VolumedownButton.grid(row = 2, column = 4, padx = 20, pady = 20)
    root.ResumeButton = Button(root,text = "Resume",background = 'LightPink', font = ('arial', 13, 'italic bold'),width = 200, bd = 5,
                            image = resume, compound = RIGHT, command = resumemusic)
    root.ResumeButton.grid(row = 1, column = 2, padx = 20, pady = 20)
    root.ResumeButton.grid_remove()

    root.MuteButton = Button(root, text="Mute", background='PaleGreen', font=('arial', 13, 'italic bold'),
                               width=100, bd=5,image = mute,compound = RIGHT,command = mutemusic)
    root.MuteButton.grid(row=3, column=5, padx=20, pady=20)
    root.MuteButton.grid_remove()


    root.UnMuteButton = Button(root, text="Unmute", background='DarkSalmon', font=('arial', 13, 'italic bold'),
                             width=100, bd=5, image=unmute, compound=RIGHT, command = unmutemusic)
    root.UnMuteButton.grid(row=3, column=5, padx=20, pady=20)
    root.UnMuteButton.grid_remove()


    ProgressLabel = Label(root, text = "", bg = "white")
    ProgressLabel.grid(row = 0, column = 5,rowspan = 3,padx=20, pady=20 )
    ProgressLabel.grid_remove()

    ProgressVolume = Progressbar(ProgressLabel,orient = VERTICAL, mode = "determinate",
                                 value = 0, length = 200)
    ProgressVolume.grid(row = 0, column = 0,ipadx = 5)

    ProgressVolumeLabel = Label(ProgressLabel, text = '0%',bg = "white",width = 3)
    ProgressVolumeLabel.grid(row = 0, column = 0)

    ProgressMusic = Label(root,text = "",bg = "white")
    ProgressMusic.grid(row = 3, column = 0,columnspan = 5,padx = 20, pady = 20)
    ProgressMusic.grid_remove()

    ProgressMusic.ProgressStart = Label(ProgressMusic, text = "00:00:00",bg = "LightPink",width = 6)
    ProgressMusic.ProgressStart.grid(row = 0, column = 0)

    ProgressMap = Progressbar(ProgressMusic,orient = HORIZONTAL, mode = "determinate", value = 0)
    ProgressMap.grid(row = 0, column = 2, ipadx = 280)

    ProgressEnd = Label(ProgressMusic, text = "00:00:00", bg = "LightPink")
    ProgressEnd.grid(row =0, column = 3)








from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import datetime
from mutagen.mp3 import MP3
from tkinter.ttk import Progressbar
from pygame import mixer
root = Tk()
root.geometry('1000x500+100+50')
root.title("Music Player....by KUSHAL MONDAL")
root.configure(bg = "black")
filename = PhotoImage(file = "background.png")
background_label = Label(root,image = filename,width = 1000)
background_label.grid(row = 0,column = 0, columnspan = 7,rowspan = 5)
root.iconbitmap("MUSIC.ico")
root.resizable(False,False)
audio = StringVar()
totalcurrlen = 0
ss = "Developed by Kushal Mondal"
count = 0
text = ''
Developer = Label(root, text = ss ,background = 'Lavender', font = ('arial', 30, 'italic bold'))
Developer.grid(row = 4, column = 1, padx = 20, pady = 20, columnspan = 4 )

def sliding():
    global count,text
    if(count >= len(ss)):
        count = -1
        text = ''
        Developer.configure(text = text)
    else:
        text = text + ss[count]
        Developer.configure(text = text)
    count += 1
    Developer.after(200,sliding)

sliding()
mixer.init()
createwidths()
root.mainloop()