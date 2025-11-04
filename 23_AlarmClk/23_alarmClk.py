import time
import datetime
import pygame
import os

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "sound.mp3"

    if not os.path.exists(sound_file):
        print("Error: Sound file not found!")
        return

    pygame.mixer.init()
    target = datetime.datetime.strptime(alarm_time, "%H:%M:%S").time()

    while True:
        now = datetime.datetime.now().time()
        print(f"\rCurrent time: {now.strftime('%H:%M:%S')}", end="")

        if now >= target:
            print("\nWAKE UP!")
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            break

        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)
