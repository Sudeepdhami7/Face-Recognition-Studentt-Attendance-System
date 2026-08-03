import os
import cv2
import mysql.connector
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from time import strftime 
from datetime import datetime
import numpy as np 


class Face_Recognition:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # ================= Title Banner =================
        title_lbl = Label(
            self.root,
            text="FACE RECOGNITION",
            font=("Times New Roman", 35, "bold"),
            bg="white",
            fg="green",
        )
        title_lbl.place(x=0, y=0, width=1530, height=50)

        # ================= Top Image (Left) =================
        try:
            img_top = Image.open(
                r"C:\Users\sudee\OneDrive\Desktop\DATA SCIENCE\face recognition\face_recognition\image4.jpg"
            )
            img_top = img_top.resize((650, 700), Image.Resampling.LANCZOS)
            self.photoimg_top = ImageTk.PhotoImage(img_top)

            f_lbl_top = Label(self.root, image=self.photoimg_top)
            f_lbl_top.place(x=0, y=55, width=650, height=700)
        except Exception:
            f_lbl_top = Label(
                self.root,
                text="LEFT BANNER IMAGE",
                bg="lightblue",
                font=("Times New Roman", 16, "bold"),
            )
            f_lbl_top.place(x=0, y=55, width=650, height=700)

        # ================= Bottom Image (Right Panel Container) =================
        try:
            img_bottom = Image.open(
                r"C:\Users\sudee\OneDrive\Desktop\DATA SCIENCE\face recognition\face_recognition\image5.jpg"
            )
            img_bottom = img_bottom.resize((880, 700), Image.Resampling.LANCZOS)
            self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

            f_lbl_bottom = Label(self.root, image=self.photoimg_bottom)
            f_lbl_bottom.place(x=650, y=55, width=880, height=700)
        except Exception:
            f_lbl_bottom = Label(
                self.root,
                text="RIGHT BANNER IMAGE",
                bg="lightgreen",
                font=("Times New Roman", 16, "bold"),
            )
            f_lbl_bottom.place(x=650, y=55, width=880, height=700)

        # ================= Action Button =================
        btn_train = Button(
            f_lbl_bottom,
            text="Face Recognition",
            command=self.face_recog,
            cursor="hand2",
            font=("Times New Roman", 20, "bold"),
            bg="darkgreen",
            fg="white",
        )
        btn_train.place(x=300, y=620, width=280, height=50)

    # ================= Attendance Logger =================
    def mark_attendance(self, i, r, n, d):
        filename = "attendance.csv"

        try:
            # 1. Create file with headers if it does not exist
            if not os.path.exists(filename):
                with open(filename, "w", newline="", encoding="utf-8") as f:
                    f.write("Student_ID,Roll,Name,Department,Time,Date,Status\n")

            # 2. Read existing IDs to prevent duplicates
            id_list = []
            with open(filename, "r", newline="", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    entry = line.strip().split(",")
                    if entry and entry[0]:
                        id_list.append(entry[0].strip())

            # 3. Append new entry using append mode ('a')
            student_id_str = str(i).strip()
            if student_id_str not in id_list:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dt_string = now.strftime("%H:%M:%S")

                with open(filename, "a", newline="", encoding="utf-8") as f:
                    f.write(f"{student_id_str},{r},{n},{d},{dt_string},{d1},Present\n")
                    print(f"Attendance marked successfully for ID: {student_id_str}")

        except PermissionError:
            print("Error: 'attendance.csv' is open in another program (e.g. Excel). Close it and try again.")
        except Exception as es:
            print(f"Error logging attendance: {es}")

    # ================= Face Recognition Function =================
    def face_recog(self):
        # Load trained classifier model
        if not os.path.exists("classifier.xml"):
            messagebox.showerror(
                "Error",
                "Training data 'classifier.xml' not found! Please train the model first.",
                parent=self.root,
            )
            return

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        # Load Haar Cascade Classifier
        cascade_file = "haarcascade_frontalface_default.xml"
        cascade_path = os.path.join(cv2.data.haarcascades, cascade_file)
        if not os.path.exists(cascade_path):
            cascade_path = cascade_file

        face_cascade = cv2.CascadeClassifier(cascade_path)

        # Establish single DB connection for the recognition session
        conn = None
        try:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="2333438",
                database="face_recognizer",
            )
            my_cursor = conn.cursor()
        except Exception as es:
            messagebox.showerror("Database Error", f"Failed to connect to database: {es}", parent=self.root)
            return

        def draw_boundary(img, classifier, scaleFactor, minNeighbors, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                id_pred, predict = clf.predict(gray_image[y : y + h, x : x + w])
                confidence = int(100 * (1 - predict / 300))

                try:
                    my_cursor.execute(
                        "SELECT Name, Roll, Dep, Student_ID FROM student WHERE Student_ID = %s",
                        (str(id_pred),),
                    )
                    row = my_cursor.fetchone()

                    if row is not None and confidence > 77:
                        n, r, d, student_id = row

                        cv2.putText(
                            img,
                            f"ID: {student_id}",
                            (x, y - 75),
                            cv2.FONT_HERSHEY_COMPLEX,
                            0.8,
                            (255, 255, 255),
                            2,
                        )
                        cv2.putText(
                            img,
                            f"Roll: {r}",
                            (x, y - 50),
                            cv2.FONT_HERSHEY_COMPLEX,
                            0.8,
                            (255, 255, 255),
                            2,
                        )
                        cv2.putText(
                            img,
                            f"Name: {n}",
                            (x, y - 25),
                            cv2.FONT_HERSHEY_COMPLEX,
                            0.8,
                            (255, 255, 255),
                            2,
                        )
                        cv2.putText(
                            img,
                            f"Department: {d}",
                            (x, y - 5),
                            cv2.FONT_HERSHEY_COMPLEX,
                            0.8,
                            (255, 255, 255),
                            2,
                        )
                        self.mark_attendance(student_id, r, n, d)
                    else:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                        cv2.putText(
                            img,
                            "Unknown Face",
                            (x, y - 5),
                            cv2.FONT_HERSHEY_COMPLEX,
                            0.8,
                            (0, 0, 255),
                            2,
                        )

                except Exception as es:
                    print(f"Database query error: {es}")

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, face_cascade):
            draw_boundary(img, face_cascade, 1.1, 10, clf)
            return img

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            if not ret:
                break

            img = recognize(img, clf, face_cascade)
            cv2.imshow("Welcome To Face Recognition", img)

            # Press Enter (13) or 'q' to exit
            key = cv2.waitKey(1)
            if key == 13 or key == ord('q'):
                break

        video_cap.release()
        cv2.destroyAllWindows()
        if conn and conn.is_connected():
            conn.close()


if __name__ == "__main__":
    root = Tk()
    app = Face_Recognition(root)
    root.mainloop()