from tkinter import filedialog
import os
import frame
from moviepy.editor import *
import audioread
from tqdm import *

audio_path = filedialog.askopenfilename()
with audioread.audio_open(audio_path) as f:
    duration = f.duration

def remover():
    counter = 0
    while counter < (duration*1000)+1:
        try:
            os.system(f"del {counter}.png")
            counter += 250
        except:
            break
    othercounter = 0
    while othercounter < (duration*1000)+1:
        try:
            os.system(f"del slicedaudio\{othercounter}.wav")
            othercounter += 250
        except:
            break

pbar = tqdm(total = duration*4)
os.system(f"cd slicedaudio && python slicer.py \"{audio_path}\"")
counter = 0
while True:
    try:
        pathname = f"D:\\04_Documents\School Documents\\11th Grade\csproject2\slicedaudio\{counter}.wav"
        frame.createframe(pathname, counter)
        counter += 250
        pbar.update(1)
    except:
        break
pbar.close()

os.system(f"python video.py {duration*1000}")

clip = VideoFileClip("final.mp4")
audioclip = AudioFileClip(audio_path)
videoclip = clip.set_audio(audioclip)
videoclip.write_videofile(f"{audio_path}.mp4")
remover()

print("Video generated!")
