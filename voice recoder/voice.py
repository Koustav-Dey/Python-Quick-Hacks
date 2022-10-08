import sounddevice
from scipy.io.wavfile import write
import tqdm
from multiprocessing import Process
import time


def loop_a(second):
    fs = 44100
    record_voice = sounddevice.rec(int(second * fs),samplerate=fs,channels=2)
    sounddevice.wait()  
    write("My_Recording.wav",fs,record_voice)

def loop_b(sec):
    print("Recording ... \n")
    for i in tqdm.tqdm(range(sec)):
        time.sleep(1)

if __name__ == '__main__':
    

    second = int(input("How many Seconds you want to record : "))

    Process(target=loop_a,args = (second,)).start()
    Process(target=loop_b,args = (second,)).start()
    

