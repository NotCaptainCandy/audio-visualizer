import librosa, librosa.display
import numpy as np

zeros = 0.0*np.arange(2001)
comparision = [list(x) for x in zip(np.arange(0,2001,1),zeros)]

def foo(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return 0

def fft(sigpath):
    use, sr = librosa.load(sigpath)
    X = np.fft.fft(use, sr+1)
    X_mag = np.absolute(X[:int(sr*0.1)+1])
    indices = X_mag > 50
    cleanxmag = X_mag * indices
    indexnum = np.arange(0, 2001, 1)
    freqdata = [list(x) for x in zip(indexnum,cleanxmag)]
    freqdata = [freqdata[x] for x in range(2001) if freqdata[x]>comparision[x]]
    try:
        maxval = max([x[1] for x in freqdata])
    except:
        maxval = 1
    freq100 = [x[1] for x in freqdata if x[0]<=100]
    freq200 = [x[1] for x in freqdata if x[0]<=200 and x[0]>100]
    freq400 = [x[1] for x in freqdata if x[0]<=400 and x[0]>200]
    freq600 = [x[1] for x in freqdata if x[0]<=600 and x[0]>400]
    freq800 = [x[1] for x in freqdata if x[0]<=800 and x[0]>600]
    freq1000 = [x[1] for x in freqdata if x[0]<=1000 and x[0]>800]
    freq1200 = [x[1] for x in freqdata if x[0]<=1200 and x[0]>1000]
    freq1400 = [x[1] for x in freqdata if x[0]<=1400 and x[0]>1200]
    freq1600 = [x[1] for x in freqdata if x[0]<=1600 and x[0]>1400]
    freq2000 = [x[1] for x in freqdata if x[0]<=2000 and x[0]>1600]
    vals = [foo(sum(freq100),len(freq100))/maxval,
            foo(sum(freq200),len(freq200))/maxval,
            foo(sum(freq400),len(freq400))/maxval,
            foo(sum(freq600),len(freq600))/maxval,
            foo(sum(freq800),len(freq800))/maxval,
            foo(sum(freq1000),len(freq1000))/maxval,
            foo(sum(freq1200),len(freq1200))/maxval,
            foo(sum(freq1400),len(freq1400))/maxval,
            foo(sum(freq1600),len(freq1600))/maxval,
            foo(sum(freq2000),len(freq2000))/maxval]
    return vals