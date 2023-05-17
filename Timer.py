import time 
sec = int(input("Enter time in sec : "))

def count_down_timer(seconds):
    while seconds>0:
    
        mins = int(seconds/60)
        secs = int(seconds%60)
    
        timer = f'{mins}:{secs}'
    
        print(timer)
        time.sleep(1)
        seconds = seconds - 1

count_down_timer(sec)
num = 5
# while num>0:
#     print(num)
#     num = num - 1

