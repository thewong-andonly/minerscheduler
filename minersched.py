from datetime import datetime
import time
import os
import sys

start_time = '00:30:00' 
end_time = '07:30:00'

print('Welcome to Ethereum Scheduler 2.0')
print(f'Mining set to start at {start_time} and set to end at {end_time}.')
print('Waiting to start...')
def miner_scheduler():
    i = 0
    while i < 2:
        current_time = datetime.now()
        now = current_time.strftime("%H:%M:%S")
        time.sleep(1)
        if i == 0: 
            if now == start_time or (now > start_time and now < end_time):
                os.startfile(r"C:\Users\micha\Documents\ethereum\etheu.bat")
                time.sleep(1)
                print('Miner started!')
                i += 1
        if i == 1:
            if now == end_time:
                os.system("taskkill /f /im EthDcrMiner64.exe") # Exits Ethereum Miner
                os.system("taskkill /f /im cmd.exe") # Closes down XMRig
                time.sleep(1)
                os.system("shutdown /s /t 1") # Shuts down PC
                quit()
                
miner_scheduler()