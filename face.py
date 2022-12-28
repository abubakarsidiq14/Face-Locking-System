import face_recognition as fr
import cv2
import os
from tkinter import *

root =Tk()
root.title("ARIES")
root.geometry('430x400')
root.config(bg='#7c7a8a')

def lock():
    cam = cv2.VideoCapture(0)

    face = fr.load_image_file("img.jpg")
    faceencd = fr.face_encodings(face)[0]

    face_encod_list = [faceencd]

    face_encod = []
    s=True
    face_coordinate = []

    while True:
        rt,frame = cam.read()

        try:
            resize_farme = cv2.resize(frame , (0,0) ,fx=0.25,fy=0.25)
            resize_farme_rgb = resize_farme[:, :, ::-1]

        except Exception as e:
            print(e)    

        if s:
            face_coordinate = fr.face_locations(resize_farme_rgb)
            face_encod = fr.face_encodings(resize_farme_rgb ,face_coordinate)

            for face in face_encod:
                matches = fr.compare_faces(face_encod_list , face)
                if matches[0] == True:
                    cam.release()
                    cv2.destroyAllWindows()
                    vspath="D:\\3103\\AI\\ARIES.py"
                    os.startfile(vspath) 
                   
        cv2.imshow("ARIES",frame)
        cv2.waitKey(1)
        if 0xFF == ord('a'):
            break

    cam.release()
    cv2.destroyAllWindows() 

Label(
    root,
    text='Press Below Button for Starting',
    font='Times 14',
    bg='#7c7a8a',
).place(x=80,y=180)

Label(
    root,
    text='Voice Assistant for Desktop',
    font='Times 24 bold',
).place(x=20,y=100)

btn = Button(
    root,
    text='Autentication',
    font='Times 18 bold',
    command=lock
).place(x=100,y=250)

root.mainloop()