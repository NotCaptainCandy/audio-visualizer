import os
import fft
import square

def createframe(filepath, num):
    os.system(f"cd finalslice\\fiveparts && python splitter.py \"{filepath}\"")
    a = fft.fft("D:\\04_Documents\School Documents\\11th Grade\csproject2\\finalslice\\fiveparts\\50.wav")
    b = fft.fft("D:\\04_Documents\School Documents\\11th Grade\csproject2\\finalslice\\fiveparts\\100.wav")
    c = fft.fft("D:\\04_Documents\School Documents\\11th Grade\csproject2\\finalslice\\fiveparts\\150.wav")
    d = fft.fft("D:\\04_Documents\School Documents\\11th Grade\csproject2\\finalslice\\fiveparts\\200.wav")
    e = fft.fft("D:\\04_Documents\School Documents\\11th Grade\csproject2\\finalslice\\fiveparts\\250.wav")
    colordata = [a,b,c,d,e]
    i = 0
    for j in colordata:    
        square.draw(j, i)
        i += 1
    square.save(num)