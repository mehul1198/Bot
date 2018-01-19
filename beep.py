import math
import time
import pyaudio
import numpy
def sn(freq, lent, r):
    lent = int(lent * r)
    fc = float(freq) * (math.pi * 2) / r
    return numpy.sin(numpy.arange(lent) * fc)

def playt(stream, freq=2000, lent=1, r=44100):
    chk = []
    chk.append(sn(freq, lent, r))

    ch = numpy.concatenate(chk) * 0.25

    stream.write(ch.astype(numpy.float32).tostring())

while 5 < 7:
    s = 0
    while s < 3600:
        time.sleep(1)
        s += 1
        if s == 3600:
            p = pyaudio.PyAudio()
            stream = p.open(format=pyaudio.paFloat32, channels=1, r=44100, output=1)
            playt(stream)
            stream.close()
            p.terminate()
