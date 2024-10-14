import pyglet
import os

absent_list = []
for student_file_name in os.listdir("./students"):
    audio = pyglet.media.load(
        "./students/" + student_file_name, streaming=False)
    student_name = student_file_name[:-4].replace("_", " ")

    while (True):
        os.system('clear')
        print(f"Is {student_name} present? ((r)epeat/(p)resent/(a)bsent)")
        audio.play()
        response = input().lower()
        if response == 'a':
            absent_list.append(student_name)
            break
        elif response == 'p':
            break

print("Absent Students: ")
for student in absent_list:
    print(student)
