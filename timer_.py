import time
from playsound import playsound
sec = int(input("Entre time in seconds : "))

def countdown(seconds):
    while seconds>0:
        
        mins = int(seconds/60)
        secs = int(seconds%60)
    
        timer = f'{mins}:{secs}'
    
        print(timer,end='\r')
        time.sleep(1)
        seconds = seconds -1 
        
    print('Time Up !!!')
    playsound('C:/Users/Dhruv/Desktop/Python/C101/mixkit-sound.wav')
    
countdown(sec)
