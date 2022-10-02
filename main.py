import moviepy.editor
from tkinter.filedialog import *
video = askopenfilename()
video = moviepy.editor.VideoFileClip(video)
audio = video.audio
a = input("Give us mp3 name : ") + ".mp3"
audio.write_audiofile(a)
print("File converted succesfully!")
