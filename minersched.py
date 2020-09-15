from datetime import datetime
import time
import os
import sys

def miner():
    print('Eth miner automater running! Waiting to start...')
    while True:
        current_time = datetime.now()
        now = current_time.strftime("%H:%M:%S")
        if now == '17:34:00':
            os.startfile(r"C:\Users\micha\Documents\ethereum\etheu.bat")
            time.sleep(1)
            print('Miner started!')
            print('Miner running!')
        if now == '17:40:00':
            os.system("taskkill /f /im EthDcrMiner64.exe")
            time.sleep(1)
            print('Mining finished!')
            miner()

miner()