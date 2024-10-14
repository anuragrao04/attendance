import pyglet
import os
from datetime import date

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


today = date.today()


with open(f"{today}.txt", "a+") as f:
    f.write("Absent Students: \n")
    for student in absent_list:
        f.write(student + "\n")


print(f"This has been stored into a file called {today}.txt")
