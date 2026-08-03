import csv
import os
import platform
import subprocess
from datetime import datetime
from time import strftime
from tkinter import *
from tkinter import filedialog, messagebox, ttk

import cv2
from PIL import Image, ImageTk

# Imports from custom project modules
try:
    from attendance import Attendance
except ImportError:
    Attendance = None

try:
    from developer import Developer
except ImportError:
    Developer = None

try:
    from face_rec import Face_Recognition
except ImportError:
    Face_Recognition = None

try:
    from help import Help
except ImportError:
    Help = None

try:
    from student import Student
except ImportError:
    Student = None

try:
    from train import Train
except ImportError:
    Train = None


class FaceRecognitionSystem:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # CCTV stream control variables
        self.cap = None
        self.is_cctv_running = False

        # Load Haar Cascade Classifier for Face Detection
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )

        # Base path relative to current working directory
        base_dir = os.path.dirname(os.path.abspath(__file__))
        img_dir = os.path.join(base_dir, "face_recognition")

        # Helper function for safe image loading
        def load_image(filename, size):
            path = os.path.join(img_dir, filename)
            if os.path.exists(path):
                img = Image.open(path)
                img = img.resize(size, Image.Resampling.LANCZOS)
                return ImageTk.PhotoImage(img)
            return None

        # ================= Top Header Images =================
        self.photoimg = load_image("agc.jpg", (500, 130))
        f_lbl = Label(self.root, image=self.photoimg, bg="gray")
        f_lbl.place(x=0, y=0, width=500, height=130)

        self.photoimg2 = load_image("images2.jpg", (500, 130))
        f_lbl2 = Label(self.root, image=self.photoimg2, bg="gray")
        f_lbl2.place(x=500, y=0, width=500, height=130)

        self.photoimg3 = load_image("images11.jpg", (500, 130))
        f_lbl3 = Label(self.root, image=self.photoimg3, bg="gray")
        f_lbl3.place(x=1000, y=0, width=500, height=130)

        # ================= Background Image =================
        self.photoimg4 = load_image("images7.jpg", (1530, 710))
        self.bg_image = Label(self.root, image=self.photoimg4, bg="lightgray")
        self.bg_image.place(x=0, y=130, width=1530, height=710)

        # ================= Main Title =================
        title_lbl = Label(
            self.bg_image,
            text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",
            font=("Times New Roman", 32, "bold"),
            bg="white",
            fg="darkgreen",
        )
        title_lbl.place(x=0, y=0, width=1530, height=50)

        # ================= Time Functionality =================
        def time():
            string = strftime("%I:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000, time)

        # Positioned at the right end to prevent text overlap
        lbl = Label(
            title_lbl,
            font=("times new roman", 13, "bold"),
            background="white",
            foreground="blue",
        )
        lbl.place(x=1380, y=0, width=140, height=50)
        time()

        # ================= TOP ROW BUTTONS =================

        # 1. Student Details
        self.photoimg5 = load_image("images10.jpg", (220, 220))
        b1 = Button(
            self.bg_image,
            image=self.photoimg5,
            command=self.student_details,
            cursor="hand2",
            bg="white",
        )
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(
            self.bg_image,
            text="Student Details",
            command=self.student_details,
            cursor="hand2",
            font=("Times New Roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b1_1.place(x=200, y=320, width=220, height=40)

        # 2. Face Detector
        self.photoimg6 = load_image("images3.jpg", (220, 220))
        b2 = Button(
            self.bg_image,
            image=self.photoimg6,
            cursor="hand2",
            command=self.face_data,
            bg="white",
        )
        b2.place(x=500, y=100, width=220, height=220)

        b2_1 = Button(
            self.bg_image,
            text="Face Detector",
            cursor="hand2",
            command=self.face_data,
            font=("Times New Roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b2_1.place(x=500, y=320, width=220, height=40)

        # 3. Attendance
        self.photoimg7 = load_image("attendance.jpg", (220, 220))
        b3 = Button(
            self.bg_image,
            image=self.photoimg7,
            cursor="hand2",
            command=self.attendance_data,
            bg="white",
        )
        b3.place(x=800, y=100, width=220, height=220)

        b3_1 = Button(
            self.bg_image,
            text="Attendance",
            cursor="hand2",
            command=self.attendance_data,
            font=("Times New Roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b3_1.place(x=800, y=320, width=220, height=40)

        # 4. Help Desk
        self.photoimg9 = load_image("help_desk.jpg", (220, 220))
        b4 = Button(
            self.bg_image,
            image=self.photoimg9,
            cursor="hand2",
            command=self.help_desk,
            bg="white",
        )
        b4.place(x=1100, y=100, width=220, height=220)

        b4_1 = Button(
            self.bg_image,
            text="Help Desk",
            cursor="hand2",
            command=self.help_desk,
            font=("Times New Roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b4_1.place(x=1100, y=320, width=220, height=40)

        # ================= BOTTOM ROW BUTTONS =================

        # 5. Train Data
        self.photoimg8 = load_image("train_data.jpg", (220, 220))
        b5 = Button(
            self.bg_image,
            image=self.photoimg8,
            cursor="hand2",
            command=self.train_data,
            bg="white",
        )
        b5.place(x=200, y=380, width=220, height=220)

        b5_1 = Button(
            self.bg_image,
            text="Train Data",
            cursor="hand2",
            command=self.train_data,
            font=("Times New Roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b5_1.place(x=200, y=600, width=220, height=40)

        # 6. Photos
        self.photoimg10 = load_image("photos.jpg", (220, 220))
        b6 = Button(
            self.bg_image,
            image=self.photoimg10,
            cursor="hand2",
            command=self.open_img,
            bg="white",
        )
        b6.place(x=500, y=380, width=220, height=220)

        b6_1 = Button(
            self.bg_image,
            text="Photos",
            cursor="hand2",
            command=self.open_img,
            font=("Times New Roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b6_1.place(x=500, y=600, width=220, height=40)

        # 7. Developer
        self.photoimg11 = load_image("developers.jpg", (220, 220))
        b7 = Button(
            self.bg_image,
            image=self.photoimg11,
            cursor="hand2",
            command=self.developer_data,
            bg="white",
        )
        b7.place(x=800, y=380, width=220, height=220)

        b7_1 = Button(
            self.bg_image,
            text="Developer",
            cursor="hand2",
            command=self.developer_data,
            font=("Times New Roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b7_1.place(x=800, y=600, width=220, height=40)

        # 8. Exit
        self.photoimg12 = load_image("exit.jpg", (220, 220))
        b8 = Button(
            self.bg_image,
            image=self.photoimg12,
            cursor="hand2",
            command=self.iExit,
            bg="white",
        )
        b8.place(x=1100, y=380, width=220, height=220)

        b8_1 = Button(
            self.bg_image,
            text="Exit",
            cursor="hand2",
            command=self.iExit,
            font=("Times New Roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        b8_1.place(x=1100, y=600, width=220, height=40)

    # ================= CCTV & Face Detection Methods =================
    def face_detector(self):
        if not self.is_cctv_running:
            cctv_source = 0  # 0 for webcam or RTSP stream link

            self.cap = cv2.VideoCapture(cctv_source)
            if not self.cap.isOpened():
                messagebox.showerror(
                    "Camera Error", "Unable to open camera stream.", parent=self.root
                )
                return

            self.is_cctv_running = True

            self.video_lbl = Label(self.bg_image, bg="black")
            self.video_lbl.place(x=365, y=70, width=800, height=550)

            self.stop_btn = Button(
                self.bg_image,
                text="CLOSE CAMERA",
                command=self.stop_cctv,
                font=("Times New Roman", 12, "bold"),
                bg="red",
                fg="white",
                cursor="hand2",
            )
            self.stop_btn.place(x=700, y=630, width=150, height=35)

            self.update_cctv_frame()
        else:
            self.stop_cctv()

    def update_cctv_frame(self):
        if self.is_cctv_running and self.cap is not None:
            ret, frame = self.cap.read()
            if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = self.face_cascade.detectMultiScale(
                    gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
                )

                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.putText(
                        frame,
                        "Face Detected",
                        (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 255, 0),
                        2,
                    )

                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame_rgb)
                img = img.resize((800, 550), Image.Resampling.LANCZOS)
                imgtk = ImageTk.PhotoImage(image=img)

                self.video_lbl.imgtk = imgtk
                self.video_lbl.configure(image=imgtk)

                self.root.after(10, self.update_cctv_frame)
            else:
                self.stop_cctv()

    def stop_cctv(self):
        self.is_cctv_running = False
        if self.cap is not None:
            self.cap.release()
            self.cap = None

        if hasattr(self, "video_lbl"):
            self.video_lbl.destroy()

        if hasattr(self, "stop_btn"):
            self.stop_btn.destroy()

    # ================= Navigation Functions =================
    def open_img(self):
        """Opens the data directory cross-platform."""
        data_path = os.path.join(os.getcwd(), "data")
        if not os.path.exists(data_path):
            os.makedirs(data_path)

        if platform.system() == "Windows":
            os.startfile(data_path)
        elif platform.system() == "Darwin":  # macOS
            subprocess.Popen(["open", data_path])
        else:  # Linux
            subprocess.Popen(["xdg-open", data_path])

    def student_details(self):
        """Opens the Student Details window."""
        if Student:
            self.new_window = Toplevel(self.root)
            self.app = Student(self.new_window)
        else:
            messagebox.showerror("Error", "Student module not found!", parent=self.root)

    def train_data(self):
        """Opens the Train Data window."""
        if Train:
            self.new_window = Toplevel(self.root)
            self.app = Train(self.new_window)
        else:
            messagebox.showerror("Error", "Train module not found!", parent=self.root)

    def face_data(self):
        """Opens the Face Recognition window."""
        if Face_Recognition:
            self.new_window = Toplevel(self.root)
            self.app = Face_Recognition(self.new_window)
        else:
            messagebox.showerror("Error", "Face Recognition module not found!", parent=self.root)

    def attendance_data(self):
        """Opens the Attendance Management window."""
        if Attendance:
            self.new_window = Toplevel(self.root)
            self.app = Attendance(self.new_window)
        else:
            messagebox.showerror("Error", "Attendance module not found!", parent=self.root)

    def developer_data(self):
        """Opens the Developer Details window."""
        if Developer:
            self.new_window = Toplevel(self.root)
            self.app = Developer(self.new_window)
        else:
            messagebox.showerror("Error", "Developer module not found!", parent=self.root)

    def help_desk(self):
        """Opens the Help Desk window."""
        if Help:
            self.new_window = Toplevel(self.root)
            self.app = Help(self.new_window)
        else:
            messagebox.showerror("Error", "Help module not found!", parent=self.root)

    def iExit(self):
        """Confirms and exits the main application."""
        confirm = messagebox.askyesno(
            "Face Recognition System",
            "Are you sure you want to exit this project?",
            parent=self.root,
        )
        if confirm:
            self.stop_cctv()
            self.root.destroy()


# Running main.py launches the Login Screen first
if __name__ == "__main__":
    from login import LoginWindow

    root = Tk()
    app = LoginWindow(root)
    root.mainloop()