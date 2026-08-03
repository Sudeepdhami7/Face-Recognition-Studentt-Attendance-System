import csv
import os
from datetime import datetime
from tkinter import *
from tkinter import filedialog, messagebox, ttk
import numpy as np
from PIL import Image, ImageTk


class Developer:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System - Attendance Management")

        # Header Title
        title_lbl = Label(
            self.root,
            text="DEVELOPER DETAILS",
            font=("times new roman", 30, "bold"),
            bg="darkblue",
            fg="white",
        )
        title_lbl.place(x=0, y=0, width=1530, height=55)

        # Top Banner / Developer Image Background
        img_path = r"C:\Users\sudee\OneDrive\Desktop\DATA SCIENCE\face recognition\face_recognition\dev.jpg"

        try:
            img_top = Image.open(img_path)
            img_top = img_top.resize((1530, 735), Image.Resampling.LANCZOS)
            self.photoimg_top = ImageTk.PhotoImage(img_top)

            self.f_lbl_top = Label(self.root, image=self.photoimg_top)
            self.f_lbl_top.place(x=0, y=55, width=1530, height=735)
        except Exception:
            # Fallback label in case the image file path is not found
            self.f_lbl_top = Label(
                self.root,
                text="DEVELOPER BACKGROUND\n(Image file not found)",
                bg="lightgrey",
                font=("Times New Roman", 18, "bold"),
            )
            self.f_lbl_top.place(x=0, y=55, width=1530, height=735)

        # Main Info Frame (Overlayed on top of the image label)
        main_frame = Frame(self.f_lbl_top, bd=2, bg="white", relief=RIDGE)
        main_frame.place(x=980, y=50, width=500, height=600)

        # Developer Info Header Inside Frame
        dev_title = Label(
            main_frame,
            text="ABOUT THE DEVELOPER",
            font=("times new roman", 20, "bold"),
            bg="white",
            fg="darkblue",
        )
        dev_title.pack(side=TOP, fill=X, pady=15)

        # Profile Image inside Frame (Optional / Fallback)
        profile_path = r"C:\Users\sudee\OneDrive\Desktop\DATA SCIENCE\face recognition\face_recognition\sudeep.jpeg"
        try:
            img_prof = Image.open(profile_path)
            img_prof = img_prof.resize((180, 180), Image.Resampling.LANCZOS)
            self.photoimg_prof = ImageTk.PhotoImage(img_prof)

            prof_lbl = Label(main_frame, image=self.photoimg_prof, bg="white")
            prof_lbl.pack(pady=10)
        except Exception:
            prof_lbl = Label(
                main_frame,
                text="[ Profile Photo ]",
                bg="lightgray",
                font=("times new roman", 12),
                width=20,
                height=8,
            )
            prof_lbl.pack(pady=10)

        # Developer Information Details
        info_label = Label(
            main_frame,
            text="Hello! I'm Sudeep.\n\n"
            "Data Science & AI Enthusiast\n"
            "Specializing in Computer Vision,\n"
            "Machine Learning & GUI Development.\n\n"
            "Tech Stack: Python, OpenCV, Tkinter, NumPy\n"
            "Contact: developer@example.com",
            font=("times new roman", 14),
            bg="white",
            justify=CENTER,
        )
        info_label.pack(pady=20, padx=20)


if __name__ == "__main__":
    root = Tk()
    app = Developer(root)
    root.mainloop()