import os
import time

def watch_directory(directory):
    print(f"Kuzatilayotgan papka: {directory}")
    files_before = set(os.listdir(directory))
    
    while True:
        time.sleep(1)
        files_after = set(os.listdir(directory))
        added_files = files_after - files_before
        removed_files = files_before - files_after
        
        if added_files:
            print(f"Yangi fayllar qo'shildi: {added_files}")
        if removed_files:
            print(f"Fayllar o'chirildi: {removed_files}")
        
        files_before = files_after


watch_directory('C:\\Users\\Isaac\\Desktop\\Cybersecurity\\MI')
