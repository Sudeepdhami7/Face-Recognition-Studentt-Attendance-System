import os
from tkinter import *
from tkinter import messagebox, ttk
import cv2  # OpenCV for handling video stream and face detection
import mysql.connector  # MySQL Database Connector
from PIL import Image, ImageTk


class Student:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Details - Face Recognition System")

        # ================= Variables =================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_student_id = StringVar()
        self.var_student_name = StringVar()
        self.var_class_div = StringVar()
        self.var_roll_no = StringVar()
        self.var_student_gender = StringVar()
        self.var_student_dob = StringVar()
        self.var_student_email = StringVar()
        self.var_student_phone = StringVar()
        self.var_student_address = StringVar()
        self.var_teacher_name = StringVar()
        self.var_radio1 = StringVar(value="No")
        self.var_search_by = StringVar()
        self.var_search_text = StringVar()
        self.is_cctv_running = False

        # ================= Top Header Image 1 =================
        try:
            img = Image.open(
                r"C:\Users\sudee\OneDrive\Desktop\DATA SCIENCE\face recognition\face_recognition\student1.jpg"
            )
            img = img.resize((500, 130), Image.Resampling.LANCZOS)
            self.photoimg = ImageTk.PhotoImage(img)

            f_lbl = Label(self.root, image=self.photoimg)
            f_lbl.place(x=0, y=0, width=500, height=130)
        except Exception:
            f_lbl = Label(
                self.root,
                text="HEADER IMAGE 1",
                bg="lightblue",
                font=("Times New Roman", 16, "bold"),
            )
            f_lbl.place(x=0, y=0, width=500, height=130)

        # ================= Top Header Image 2 =================
        try:
            img2 = Image.open(
                r"C:\Users\sudee\OneDrive\Desktop\DATA SCIENCE\face recognition\face_recognition\student3.jpg"
            )
            img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
            self.photoimg2 = ImageTk.PhotoImage(img2)

            f_lbl2 = Label(self.root, image=self.photoimg2)
            f_lbl2.place(x=500, y=0, width=500, height=130)
        except Exception:
            f_lbl2 = Label(
                self.root,
                text="HEADER IMAGE 2",
                bg="lightgreen",
                font=("Times New Roman", 16, "bold"),
            )
            f_lbl2.place(x=500, y=0, width=500, height=130)

        # ================= Top Header Image 3 =================
        try:
            img3 = Image.open(
                r"C:\Users\sudee\OneDrive\Desktop\DATA SCIENCE\face recognition\face_recognition\student2.jpg"
            )
            img3 = img3.resize((500, 130), Image.Resampling.LANCZOS)
            self.photoimg3 = ImageTk.PhotoImage(img3)

            f_lbl3 = Label(self.root, image=self.photoimg3)
            f_lbl3.place(x=1000, y=0, width=500, height=130)
        except Exception:
            f_lbl3 = Label(
                self.root,
                text="HEADER IMAGE 3",
                bg="lightyellow",
                font=("Times New Roman", 16, "bold"),
            )
            f_lbl3.place(x=1000, y=0, width=500, height=130)

        # ================= Background Image =================
        try:
            img4 = Image.open(
                r"C:\Users\sudee\OneDrive\Desktop\DATA SCIENCE\face recognition\face_recognition\bg.jpg"
            )
            img4 = img4.resize((1530, 710), Image.Resampling.LANCZOS)
            self.photoimg4 = ImageTk.PhotoImage(img4)

            bg_image = Label(self.root, image=self.photoimg4)
            bg_image.place(x=0, y=130, width=1530, height=710)
        except Exception:
            bg_image = Label(self.root, bg="gray")
            bg_image.place(x=0, y=130, width=1530, height=710)

        # ================= Main Title =================
        title_lbl = Label(
            bg_image,
            text="STUDENT MANAGEMENT SYSTEM",
            font=("Times New Roman", 35, "bold"),
            bg="white",
            fg="darkgreen",
        )
        title_lbl.place(x=0, y=0, width=1530, height=50)

        # ================= Main Frame Container =================
        main_frame = Frame(bg_image, bd=2, bg="white")
        main_frame.place(x=20, y=55, width=1480, height=600)

        # ================= Left Label Frame =================
        Left_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Student Details",
            font=("Times New Roman", 12, "bold"),
        )
        Left_frame.place(x=10, y=10, width=730, height=580)

        try:
            img_left = Image.open(
                r"C:\Users\sudee\OneDrive\Desktop\DATA SCIENCE\face recognition\face_recognition\student5.jpg"
            )
            img_left = img_left.resize((710, 130), Image.Resampling.LANCZOS)
            self.photoimg_left = ImageTk.PhotoImage(img_left)

            f_lbl_left = Label(Left_frame, image=self.photoimg_left)
            f_lbl_left.place(x=5, y=0, width=710, height=130)
        except Exception:
            f_lbl_left = Label(
                Left_frame,
                text="STUDENT BANNER",
                bg="lightgray",
                font=("Times New Roman", 14, "bold"),
            )
            f_lbl_left.place(x=5, y=0, width=710, height=130)

        # ================= Current Course Information =================
        Current_Course_frame = LabelFrame(
            Left_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Current Course Information",
            font=("Times New Roman", 12, "bold"),
        )
        Current_Course_frame.place(x=5, y=135, width=710, height=115)

        dep_label = Label(
            Current_Course_frame,
            text="Department",
            font=("Times New Roman", 12, "bold"),
            bg="white",
        )
        dep_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        dep_combo = ttk.Combobox(
            Current_Course_frame,
            textvariable=self.var_dep,
            font=("Times New Roman", 11, "bold"),
            state="readonly",
            width=18,
        )
        dep_combo["values"] = (
            "Select Department",
            "Computer Science",
            "Applied Sciences",
            "Civil Engineering",
            "Mechanical Engineering",
        )
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        course_label = Label(
            Current_Course_frame,
            text="Course",
            font=("Times New Roman", 12, "bold"),
            bg="white",
        )
        course_label.grid(row=0, column=2, padx=15, pady=5, sticky=W)

        course_combo = ttk.Combobox(
            Current_Course_frame,
            textvariable=self.var_course,
            font=("Times New Roman", 11, "bold"),
            state="readonly",
            width=18,
        )
        course_combo["values"] = ("Select Course", "B.Tech", "M.Tech", "B.A", "M.A")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        year_label = Label(
            Current_Course_frame,
            text="Year",
            font=("Times New Roman", 12, "bold"),
            bg="white",
        )
        year_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        year_combo = ttk.Combobox(
            Current_Course_frame,
            textvariable=self.var_year,
            font=("Times New Roman", 11, "bold"),
            state="readonly",
            width=18,
        )
        year_combo["values"] = (
            "Select Year",
            "2020-21",
            "2021-22",
            "2022-23",
            "2023-24",
            "2024-25",
            "2025-26",
            "2026-27",
            "2027-28",
        )
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        semester_label = Label(
            Current_Course_frame,
            text="Semester",
            font=("Times New Roman", 12, "bold"),
            bg="white",
        )
        semester_label.grid(row=1, column=2, padx=15, pady=5, sticky=W)

        semester_combo = ttk.Combobox(
            Current_Course_frame,
            textvariable=self.var_semester,
            font=("Times New Roman", 11, "bold"),
            state="readonly",
            width=18,
        )
        semester_combo["values"] = (
            "Select Semester",
            "1st Semester",
            "2nd Semester",
            "3rd Semester",
            "4th Semester",
            "5th Semester",
            "6th Semester",
            "7th Semester",
            "8th Semester",
        )
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        # ================= Class Student Information =================
        Class_Student_frame = LabelFrame(
            Left_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Class Student Information",
            font=("Times New Roman", 12, "bold"),
        )
        Class_Student_frame.place(x=5, y=250, width=710, height=300)

        # --- Row 0 ---
        studentID_Label = Label(
            Class_Student_frame,
            text="Student ID:",
            font=("Times New Roman", 12, "bold"),
            bg="white",
        )
        studentID_Label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        studentID_entry = ttk.Entry(
            Class_Student_frame,
            textvariable=self.var_student_id,
            width=18,
            font=("Times New Roman", 11, "bold"),
        )
        studentID_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        studentName_Label = Label(
            Class_Student_frame,
            text="Student Name:",
            font=("Times New Roman", 12, "bold"),
            bg="white",
        )
        studentName_Label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        studentName_entry = ttk.Entry(
            Class_Student_frame,
            textvariable=self.var_student_name,
            width=18,
            font=("Times New Roman", 11, "bold"),
        )
        studentName_entry.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        # --- Row 1 ---
        class_div_Label = Label(
            Class_Student_frame,
            text="Class Division:",
            font=("Times New Roman", 12, "bold"),
            bg="white",
        )
        class_div_Label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        class_div_entry = ttk.Entry(
            Class_Student_frame,
            textvariable=self.var_class_div,
            width=18,
            font=("Times New Roman", 11, "bold"),
        )
        class_div_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        roll_no_Label = Label(
            Class_Student_frame,
            text="Roll No:",
            font=("Times New Roman", 12, "bold"),
            bg="white",
        )
        roll_no_Label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        roll_no_entry = ttk.Entry(
            Class_Student_frame,
            textvariable=self.var_roll_no,
            width=18,
            font=("Times New Roman", 11, "bold"),
        )
        roll_no_entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        # --- Row 2 ---
        gender_Label = Label(
            Class_Student_frame,
            text="Gender:",
            font=("Times New Roman", 12, "bold"),
            bg="white",
        )
        gender_Label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(
            Class_Student_frame,
            textvariable=self.var_student_gender,
            font=("Times New Roman", 11, "bold"),
            state="readonly",
            width=16,
        )
        gender_combo["values"] = ("Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        dob_Label = Label(
            Class_Student_frame,
            text="DOB:",
            font=("Times New Roman", 12, "bold"),
            bg="white",
        )
        dob_Label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        dob_entry = ttk.Entry(
            Class_Student_frame,
            textvariable=self.var_student_dob,
            width=18,
            font=("Times New Roman", 11, "bold"),
        )
        dob_entry.grid(row=2, column=3, padx=5, pady=5, sticky=W)

        # --- Row 3 ---
        email_Label = Label(
            Class_Student_frame,
            text="Email:",
            font=("Times New Roman", 12, "bold"),
            bg="white",
        )
        email_Label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        email_entry = ttk.Entry(
            Class_Student_frame,
            textvariable=self.var_student_email,
            width=18,
            font=("Times New Roman", 11, "bold"),
        )
        email_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        phone_Label = Label(
            Class_Student_frame,
            text="Phone Number:",
            font=("Times New Roman", 12, "bold"),
            bg="white",
        )
        phone_Label.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        phone_entry = ttk.Entry(
            Class_Student_frame,
            textvariable=self.var_student_phone,
            width=18,
            font=("Times New Roman", 11, "bold"),
        )
        phone_entry.grid(row=3, column=3, padx=5, pady=5, sticky=W)

        # --- Row 4 ---
        address_Label = Label(
            Class_Student_frame,
            text="Address:",
            font=("Times New Roman", 12, "bold"),
            bg="white",
        )
        address_Label.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        address_entry = ttk.Entry(
            Class_Student_frame,
            textvariable=self.var_student_address,
            width=18,
            font=("Times New Roman", 11, "bold"),
        )
        address_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)

        teacher_Label = Label(
            Class_Student_frame,
            text="Teacher Name:",
            font=("Times New Roman", 12, "bold"),
            bg="white",
        )
        teacher_Label.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        teacher_entry = ttk.Entry(
            Class_Student_frame,
            textvariable=self.var_teacher_name,
            width=18,
            font=("Times New Roman", 11, "bold"),
        )
        teacher_entry.grid(row=4, column=3, padx=5, pady=5, sticky=W)

        # --- Row 5 ---
        radiobtn1 = ttk.Radiobutton(
            Class_Student_frame,
            text="Take Photo Sample",
            variable=self.var_radio1,
            value="Yes",
        )
        radiobtn1.grid(row=5, column=0, padx=10, pady=5, sticky=W)

        radiobtn2 = ttk.Radiobutton(
            Class_Student_frame,
            text="No Photo Sample",
            variable=self.var_radio1,
            value="No",
        )
        radiobtn2.grid(row=5, column=1, padx=10, pady=5, sticky=W)

        # ================= First Row Buttons =================
        btn_frame = Frame(Class_Student_frame, bd=2, bg="white", relief=RIDGE)
        btn_frame.place(x=0, y=195, width=700, height=35)

        save_btn = Button(
            btn_frame,
            text="Save",
            command=self.add_data,
            font=("Times New Roman", 12, "bold"),
            bg="blue",
            fg="white",
            width=15,
        )
        save_btn.grid(row=0, column=0, padx=5, pady=2)

        update_btn = Button(
            btn_frame,
            text="Update",
            command=self.update_data,
            font=("Times New Roman", 12, "bold"),
            bg="green",
            fg="white",
            width=15,
        )
        update_btn.grid(row=0, column=1, padx=5, pady=2)

        delete_btn = Button(
            btn_frame,
            text="Delete",
            command=self.delete_data,
            font=("Times New Roman", 12, "bold"),
            bg="red",
            fg="white",
            width=15,
        )
        delete_btn.grid(row=0, column=2, padx=5, pady=2)

        reset_btn = Button(
            btn_frame,
            text="Reset",
            command=self.reset_data,
            font=("Times New Roman", 12, "bold"),
            bg="orange",
            fg="white",
            width=15,
        )
        reset_btn.grid(row=0, column=3, padx=5, pady=2)

        # ================= Second Row Buttons =================
        btn_frame1 = Frame(Class_Student_frame, bd=2, bg="white", relief=RIDGE)
        btn_frame1.place(x=0, y=230, width=700, height=40)

        take_photo_btn = Button(
            btn_frame1,
            text="Take Photo Sample",
            command=self.generate_dataset,
            font=("Times New Roman", 11, "bold"),
            bg="darkblue",
            fg="white",
            width=21,
        )
        take_photo_btn.grid(row=0, column=0, padx=4, pady=2)

        update_photo_btn = Button(
            btn_frame1,
            text="Update Photo Sample",
            command=self.generate_dataset,
            font=("Times New Roman", 11, "bold"),
            bg="darkgreen",
            fg="white",
            width=21,
        )
        update_photo_btn.grid(row=0, column=1, padx=4, pady=2)

        cctv_btn = Button(
            btn_frame1,
            text="Mark Attendance (CCTV)",
            command=self.open_cctv_stream,
            font=("Times New Roman", 11, "bold"),
            bg="purple",
            fg="white",
            width=22,
        )
        cctv_btn.grid(row=0, column=2, padx=4, pady=2)

        # ================= Right Label Frame =================
        Right_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Student Details",
            font=("Times New Roman", 12, "bold"),
        )
        Right_frame.place(x=750, y=10, width=720, height=580)

        try:
            img_Right = Image.open(
                r"C:\Users\sudee\OneDrive\Desktop\DATA SCIENCE\face recognition\face_recognition\S1.jpg"
            )
            img_Right = img_Right.resize((710, 130), Image.Resampling.LANCZOS)
            self.photoimg_Right = ImageTk.PhotoImage(img_Right)

            f_lbl_Right = Label(Right_frame, image=self.photoimg_Right)
            f_lbl_Right.place(x=5, y=0, width=710, height=130)
        except Exception:
            f_lbl_Right = Label(
                Right_frame,
                text="RIGHT BANNER",
                bg="lightpink",
                font=("Times New Roman", 14, "bold"),
            )
            f_lbl_Right.place(x=5, y=0, width=710, height=130)

        # --- Search System ---
        search_frame = LabelFrame(
            Right_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Search System",
            font=("Times New Roman", 11, "bold"),
        )
        search_frame.place(x=5, y=135, width=700, height=70)

        search_label = Label(
            search_frame,
            text="Search By:",
            font=("Times New Roman", 11, "bold"),
            bg="red",
            fg="white",
        )
        search_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        search_combo = ttk.Combobox(
            search_frame,
            textvariable=self.var_search_by,
            font=("Times New Roman", 10, "bold"),
            state="readonly",
            width=12,
        )
        search_combo["values"] = (
            "Select Option",
            "Roll No",
            "Phone No",
            "Student ID",
        )
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        search_entry = ttk.Entry(
            search_frame,
            textvariable=self.var_search_text,
            width=15,
            font=("Times New Roman", 10, "bold"),
        )
        search_entry.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        search_btn = Button(
            search_frame,
            text="Search",
            command=self.search_data,
            font=("Times New Roman", 10, "bold"),
            bg="blue",
            fg="white",
            width=10,
        )
        search_btn.grid(row=0, column=3, padx=3, pady=5)

        showAll_btn = Button(
            search_frame,
            text="Show All",
            command=self.fetch_data,
            font=("Times New Roman", 10, "bold"),
            bg="darkgreen",
            fg="white",
            width=10,
        )
        showAll_btn.grid(row=0, column=4, padx=3, pady=5)

        # --- Table Frame ---
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=700, height=340)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(
            table_frame,
            column=(
                "dep",
                "course",
                "year",
                "sem",
                "id",
                "name",
                "div",
                "roll",
                "gender",
                "dob",
                "email",
                "phone",
                "address",
                "teacher",
                "photo",
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="Photo Status")

        self.student_table["show"] = "headings"
        self.student_table.pack(fill=BOTH, expand=1)

        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def get_db_connection(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="2333438",
            database="face_recognizer",
        )

    # ================= Database Methods =================
    def add_data(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_student_id.get() == ""
        ):
            messagebox.showerror(
                "Error",
                "All Fields (Department & Student ID) are required!",
                parent=self.root,
            )
        else:
            try:
                conn = self.get_db_connection()
                my_cursor = conn.cursor()
                my_cursor.execute("""CREATE TABLE IF NOT EXISTS student (
                            Dep VARCHAR(45), Course VARCHAR(45), Year VARCHAR(45),
                            Semester VARCHAR(45), Student_ID VARCHAR(45) PRIMARY KEY,
                            Name VARCHAR(45), Division VARCHAR(45), Roll VARCHAR(45),
                            Gender VARCHAR(45), DOB VARCHAR(45), Email VARCHAR(45),
                            Phone VARCHAR(45), Address VARCHAR(45), Teacher VARCHAR(45),
                            PhotoSample VARCHAR(45)
                        )""")

                my_cursor.execute(
                    """INSERT INTO student (
                            Dep, Course, Year, Semester, Student_ID, Name, Division, 
                            Roll, Gender, DOB, Email, Phone, Address, Teacher, PhotoSample
                        ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_student_id.get(),
                        self.var_student_name.get(),
                        self.var_class_div.get(),
                        self.var_roll_no.get(),
                        self.var_student_gender.get(),
                        self.var_student_dob.get(),
                        self.var_student_email.get(),
                        self.var_student_phone.get(),
                        self.var_student_address.get(),
                        self.var_teacher_name.get(),
                        self.var_radio1.get(),
                    ),
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success",
                    "Student details added successfully!",
                    parent=self.root,
                )
            except mysql.connector.Error as err:
                if err.errno == 1062:
                    messagebox.showerror(
                        "Error",
                        f"Student ID '{self.var_student_id.get()}' already exists!",
                        parent=self.root,
                    )
                else:
                    messagebox.showerror(
                        "Error", f"Database Error: {str(err)}", parent=self.root
                    )
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to: {str(es)}", parent=self.root
                )

    def fetch_data(self):
        try:
            conn = self.get_db_connection()
            my_cursor = conn.cursor()
            my_cursor.execute(
                "SELECT Dep, Course, Year, Semester, Student_ID, Name, Division,"
                " Roll, Gender, DOB, Email, Phone, Address, Teacher, PhotoSample FROM"
                " student"
            )
            data = my_cursor.fetchall()
            if len(data) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("", END, values=i)
                conn.commit()
            conn.close()
        except Exception:
            pass

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        if data:
            self.var_dep.set(data[0])
            self.var_course.set(data[1])
            self.var_year.set(data[2])
            self.var_semester.set(data[3])
            self.var_student_id.set(data[4])
            self.var_student_name.set(data[5])
            self.var_class_div.set(data[6])
            self.var_roll_no.set(data[7])
            self.var_student_gender.set(data[8])
            self.var_student_dob.set(data[9])
            self.var_student_email.set(data[10])
            self.var_student_phone.set(data[11])
            self.var_student_address.set(data[12])
            self.var_teacher_name.set(data[13])
            self.var_radio1.set(data[14])

    def update_data(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_student_id.get() == ""
        ):
            messagebox.showerror(
                "Error",
                "Select a record from table to update!",
                parent=self.root,
            )
        else:
            try:
                if (
                    messagebox.askyesno(
                        "Update",
                        "Update this record?",
                        parent=self.root,
                    )
                    > 0
                ):
                    conn = self.get_db_connection()
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        """UPDATE student SET Dep=%s, Course=%s, Year=%s, Semester=%s, 
                                    Name=%s, Division=%s, Roll=%s, Gender=%s, DOB=%s, Email=%s, 
                                    Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_ID=%s""",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_student_name.get(),
                            self.var_class_div.get(),
                            self.var_roll_no.get(),
                            self.var_student_gender.get(),
                            self.var_student_dob.get(),
                            self.var_student_email.get(),
                            self.var_student_phone.get(),
                            self.var_student_address.get(),
                            self.var_teacher_name.get(),
                            self.var_radio1.get(),
                            self.var_student_id.get(),
                        ),
                    )
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo(
                        "Success",
                        "Record updated successfully!",
                        parent=self.root,
                    )
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to: {str(es)}", parent=self.root
                )

    def delete_data(self):
        if self.var_student_id.get() == "":
            messagebox.showerror(
                "Error", "Student ID is required!", parent=self.root
            )
        else:
            try:
                if (
                    messagebox.askyesno(
                        "Delete",
                        "Delete this record?",
                        parent=self.root,
                    )
                    > 0
                ):
                    conn = self.get_db_connection()
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "DELETE FROM student WHERE Student_ID=%s",
                        (self.var_student_id.get(),),
                    )
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    self.reset_data()
                    messagebox.showinfo(
                        "Delete",
                        "Record deleted successfully!",
                        parent=self.root,
                    )
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to: {str(es)}", parent=self.root
                )

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_student_id.set("")
        self.var_student_name.set("")
        self.var_class_div.set("")
        self.var_roll_no.set("")
        self.var_student_gender.set("Male")
        self.var_student_dob.set("")
        self.var_student_email.set("")
        self.var_student_phone.set("")
        self.var_student_address.set("")
        self.var_teacher_name.set("")
        self.var_radio1.set("No")
        self.var_search_by.set("Select Option")
        self.var_search_text.set("")

    def search_data(self):
        if (
            self.var_search_by.get() == "Select Option"
            or self.var_search_text.get() == ""
        ):
            messagebox.showerror(
                "Error",
                "Select Search By option and enter text!",
                parent=self.root,
            )
        else:
            try:
                column_map = {
                    "Roll No": "Roll",
                    "Phone No": "Phone",
                    "Student ID": "Student_ID",
                }
                search_col = column_map.get(self.var_search_by.get())
                conn = self.get_db_connection()
                my_cursor = conn.cursor()
                my_cursor.execute(
                    f"SELECT Dep, Course, Year, Semester, Student_ID, Name, Division,"
                    f" Roll, Gender, DOB, Email, Phone, Address, Teacher, PhotoSample"
                    f" FROM student WHERE {search_col} LIKE %s",
                    (f"%{self.var_search_text.get()}%",),
                )
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for row in rows:
                        self.student_table.insert("", END, values=row)
                    conn.commit()
                else:
                    messagebox.showinfo(
                        "Search", "No records found.", parent=self.root
                    )
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to: {str(es)}", parent=self.root
                )

    # ================= Generate Photo Dataset Method =================
    def generate_dataset(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_student_id.get() == ""
        ):
            messagebox.showerror(
                "Error",
                "Please enter Student ID and Department first!",
                parent=self.root,
            )
        else:
            try:
                conn = self.get_db_connection()
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "SELECT * FROM student WHERE Student_ID=%s",
                    (self.var_student_id.get(),),
                )
                my_result = my_cursor.fetchone()

                if my_result is None:
                    messagebox.showerror(
                        "Error",
                        "Student ID not found in database. Click 'Save' first!",
                        parent=self.root,
                    )
                    conn.close()
                    return

                my_cursor.execute(
                    "UPDATE student SET PhotoSample='Yes' WHERE Student_ID=%s",
                    (self.var_student_id.get(),),
                )
                conn.commit()
                self.fetch_data()
                conn.close()

                cascade_file = "haarcascade_frontalface_default.xml"
                cascade_path = os.path.join(cv2.data.haarcascades, cascade_file)
                if not os.path.exists(cascade_path):
                    cascade_path = cascade_file

                face_classifier = cv2.CascadeClassifier(cascade_path)
                if face_classifier.empty():
                    messagebox.showerror(
                        "Error",
                        f"Could not load Haar Cascade XML model file ('{cascade_file}').",
                        parent=self.root,
                    )
                    return

                if not os.path.exists("data"):
                    os.makedirs("data")

                cap = cv2.VideoCapture(0)
                if not cap.isOpened():
                    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if not ret or my_frame is None:
                        break

                    gray = cv2.cvtColor(my_frame, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(
                        gray, scaleFactor=1.3, minNeighbors=5
                    )

                    for x, y, w, h in faces:
                        img_id += 1
                        face_cut = gray[y : y + h, x : x + w]
                        face_cut = cv2.resize(face_cut, (450, 450))

                        file_path = f"data/user.{self.var_student_id.get()}.{img_id}.jpg"
                        cv2.imwrite(file_path, face_cut)

                        cv2.rectangle(
                            my_frame, (x, y), (x + w, y + h), (0, 255, 0), 2
                        )
                        cv2.putText(
                            my_frame,
                            f"Samples Taken: {img_id}/100",
                            (50, 50),
                            cv2.FONT_HERSHEY_COMPLEX,
                            0.8,
                            (0, 255, 0),
                            2,
                        )

                    cv2.imshow("Capturing Face Samples - Press 'Enter' or Wait for 100", my_frame)
                    if cv2.waitKey(1) == 13 or img_id == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                self.var_radio1.set("Yes")
                messagebox.showinfo(
                    "Result",
                    f"Successfully captured {img_id} photo samples!",
                    parent=self.root,
                )
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to: {str(es)}", parent=self.root
                )

    # ================= CCTV Video Feed Method =================
    def open_cctv_stream(self):
        cctv_window = Toplevel(self.root)
        cctv_window.title("CCTV Live Attendance Stream")
        cctv_window.geometry("660x550")

        video_lbl = Label(cctv_window, bg="black")
        video_lbl.pack(fill=BOTH, expand=True, padx=10, pady=10)

        cascade_file = "haarcascade_frontalface_default.xml"
        cascade_path = os.path.join(cv2.data.haarcascades, cascade_file)
        if not os.path.exists(cascade_path):
            cascade_path = cascade_file

        face_classifier = cv2.CascadeClassifier(cascade_path)

        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        self.is_cctv_running = True

        def update_stream():
            if self.is_cctv_running and cap is not None and cap.isOpened():
                ret, frame = cap.read()
                if ret and frame is not None and frame.size > 0:
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(
                        gray, scaleFactor=1.3, minNeighbors=5
                    )

                    for x, y, w, h in faces:
                        cv2.rectangle(
                            frame, (x, y), (x + w, y + h), (0, 255, 0), 2
                        )
                        cv2.putText(
                            frame,
                            "Face Detected",
                            (x, y - 10),
                            cv2.FONT_HERSHEY_COMPLEX,
                            0.8,
                            (0, 255, 0),
                            2,
                        )

                    frame = cv2.resize(frame, (640, 440))
                    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    img = Image.fromarray(rgb_frame)
                    imgtk = ImageTk.PhotoImage(image=img)

                    video_lbl.imgtk = imgtk
                    video_lbl.configure(image=imgtk, text="")
                    video_lbl.after(15, update_stream)
                    return

            video_lbl.configure(
                image="",
                text=(
                    "CAMERA FEED UNAVAILABLE\n\n"
                    "1. Ensure no other application (Zoom, Teams, Browser) is using the webcam.\n"
                    "2. Verify camera permissions under Windows Settings > Privacy."
                ),
                fg="yellow",
                bg="black",
                font=("Times New Roman", 12, "bold"),
            )

        def close_stream():
            self.is_cctv_running = False
            if cap is not None and cap.isOpened():
                cap.release()
            cctv_window.destroy()

        cctv_window.protocol("WM_DELETE_WINDOW", close_stream)

        close_btn = Button(
            cctv_window,
            text="CLOSE CAMERA",
            command=close_stream,
            bg="red",
            fg="white",
            font=("Times New Roman", 11, "bold"),
        )
        close_btn.pack(pady=5)

        update_stream()


if __name__ == "__main__":
    root = Tk()
    app = Student(root)
    root.mainloop()