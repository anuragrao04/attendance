import os
import shutil
from gtts import gTTS
from concurrent.futures import ThreadPoolExecutor
# if exists, remove
if (os.path.exists("students")):
    shutil.rmtree("./students")
os.mkdir("students")
students = []

print("How many students are in your class? ")
n = input()
# check if windows
if (os.name == 'nt'):
    os.system("cls")
else:
    os.system("clear")

print("Enter Student List, one name per line (You can copy and paste from your google sheet): ")
for i in range(int(n)):
    student = input().strip().lower()
    students.append(student)

if (os.name == 'nt'):
    os.system("cls")
else:
    os.system("clear")

print("Awesome, now generating audio files for your student list... Give me a min")


def generate_audio(student):
    """Generates and saves the TTS audio for a single student."""
    student, srn = student.split("\t")
    student_file_name = student.replace(" ", "_")
    tts = gTTS(student, lang='en')
    tts.save(f"./students/{student_file_name}.mp3")
    print(f"Generated audio for {student}")


with ThreadPoolExecutor(max_workers=4) as executor:
    executor.map(generate_audio, students)


print("Done! You can now run main.py anytime you want to take attendance")
