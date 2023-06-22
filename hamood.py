from PIL import Image
from pydub import AudioSegment
from pydub.playback import play
import os
import pydub

ffmpeg_path = r"C:\Users\PC TP\OneDrive\Desktop\ffmpeg-6.0\bin\ffmpeg"

# Add FFmpeg folder path to the system's PATH environment variable
os.environ["PATH"] += os.pathsep + os.path.dirname(ffmpeg_path)

# Set the FFmpeg executable path in PyDub
pydub.AudioSegment.ffmpeg = ffmpeg_path

user_list = ['farhan', 'eshan', 'max']
print("Enter your username:")
user = input()

if user not in user_list:
    print("Create a password:")
    password = input()
    print("Confirm your password:")
    confirm_password = input()

    if password == confirm_password:
        print("Thanks for creating an account.")
        user_list.append(user)
    else:
        print("Try again later.")
else:
    print("Username already exists.")

print(user_list, "Your username is added to the list.")


image_path = r"C:\Users\PC TP\OneDrive\Pictures\download.jpg"
image = Image.open(image_path)
image.show()


audio_path = r"C:\Users\PC TP\Downloads\HamoudHabibiMp3Ringtone1358567608.mp3"
audio = AudioSegment.from_file(audio_path)
play(audio)
