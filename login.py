import csv
import os
from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

# DO NOT import FaceRecognitionSystem here at top-level to prevent circular imports!

USER_DATA_FILE = "users.csv"

# Ensure user database CSV file exists with headers
if not os.path.exists(USER_DATA_FILE):
    with open(USER_DATA_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "fname", "lname", "contact", "email", 
            "security_q", "security_a", "password"
        ])


class LoginWindow:

    def __init__(self, root):
        self.root = root
        self.root.title("Login - Face Recognition System")
        self.root.geometry("1530x790+0+0")
        self.root.configure(bg="#1d212a")

        # Login Variables
        self.var_login_email = StringVar()
        self.var_login_password = StringVar()

        # ================= Background Image =================
        base_dir = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(base_dir, "face_recognition", "login_bg.jpg")

        try:
            bg_img = Image.open(img_path)
            bg_img = bg_img.resize((1530, 790), Image.Resampling.LANCZOS)
            self.photo_bg = ImageTk.PhotoImage(bg_img)
            bg_lbl = Label(self.root, image=self.photo_bg)
            bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception:
            bg_lbl = Label(self.root, bg="#1a1c23")
            bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # ================= Login Card =================
        frame = Frame(self.root, bg="white", bd=2, relief=RIDGE)
        frame.place(x=540, y=150, width=450, height=500)

        heading = Label(
            frame,
            text="USER LOGIN",
            font=("times new roman", 24, "bold"),
            bg="white",
            fg="darkblue",
        )
        heading.place(x=0, y=25, width=450)

        # Form Fields
        lbl_user = Label(
            frame,
            text="Email / Username",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        lbl_user.place(x=50, y=100)

        txt_user = Entry(
            frame,
            textvariable=self.var_login_email,
            font=("times new roman", 12),
            bg="#f2f2f2",
            bd=1,
            relief=GROOVE,
        )
        txt_user.place(x=50, y=130, width=350, height=35)

        lbl_pass = Label(
            frame,
            text="Password",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        lbl_pass.place(x=50, y=180)

        txt_pass = Entry(
            frame,
            textvariable=self.var_login_password,
            font=("times new roman", 12),
            bg="#f2f2f2",
            show="*",
            bd=1,
            relief=GROOVE,
        )
        txt_pass.place(x=50, y=210, width=350, height=35)

        # Login Action Button
        login_btn = Button(
            frame,
            text="LOG IN",
            command=self.login_action,
            font=("times new roman", 13, "bold"),
            bg="darkblue",
            fg="white",
            cursor="hand2",
            bd=0,
        )
        login_btn.place(x=50, y=270, width=350, height=40)

        # Registration & Reset Options
        register_btn = Button(
            frame,
            text="New User Register",
            command=self.register_window,
            font=("times new roman", 11, "bold"),
            bg="white",
            fg="darkgreen",
            bd=0,
            cursor="hand2",
        )
        register_btn.place(x=50, y=330)

        forgot_btn = Button(
            frame,
            text="Forgot Password?",
            command=self.forgot_password_window,
            font=("times new roman", 11, "bold"),
            bg="white",
            fg="red",
            bd=0,
            cursor="hand2",
        )
        forgot_btn.place(x=280, y=330)

    # ================= Login Logic =================
    def login_action(self):
        email = self.var_login_email.get().strip()
        password = self.var_login_password.get().strip()

        if email == "" or password == "":
            messagebox.showerror("Error", "Please fill in all fields!", parent=self.root)
            return

        # Default fallback admin
        if email == "Admin" and password == "12345":
            self.success_login("Admin")
            return

        # Check registered users in CSV
        found = False
        try:
            with open(USER_DATA_FILE, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader, None)  # Skip header
                for row in reader:
                    if row and (row[3] == email or row[0] == email) and row[6] == password:
                        found = True
                        self.success_login(row[0])
                        break
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read user data: {e}", parent=self.root)

        if not found:
            messagebox.showerror("Access Denied", "Invalid Email or Password!", parent=self.root)

    def success_login(self, username):
        messagebox.showinfo("Success", f"Welcome back, {username}!", parent=self.root)
        self.root.destroy()
        
        # Local import inside function breaks the circular dependency chain!
        from main import FaceRecognitionSystem
        
        main_root = Tk()
        app = FaceRecognitionSystem(main_root)
        main_root.mainloop()

    # ================= Registration Window =================
    def register_window(self):
        self.reg_win = Toplevel(self.root)
        self.reg_win.title("Register New User")
        self.reg_win.geometry("800x550+350+120")
        self.reg_win.configure(bg="white")
        self.reg_win.grab_set()

        # Registration Variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_security_q = StringVar()
        self.var_security_a = StringVar()
        self.var_reg_pass = StringVar()
        self.var_reg_cpass = StringVar()
        self.var_check = IntVar()

        title = Label(
            self.reg_win,
            text="REGISTER HERE",
            font=("times new roman", 22, "bold"),
            bg="white",
            fg="darkgreen",
        )
        title.place(x=30, y=20)

        # Form Controls (Two Columns)
        # Row 1
        Label(self.reg_win, text="First Name", font=("times new roman", 11, "bold"), bg="white").place(x=50, y=80)
        Entry(self.reg_win, textvariable=self.var_fname, font=("times new roman", 11), bg="#f8f8f8").place(x=50, y=105, width=320, height=30)

        Label(self.reg_win, text="Last Name", font=("times new roman", 11, "bold"), bg="white").place(x=420, y=80)
        Entry(self.reg_win, textvariable=self.var_lname, font=("times new roman", 11), bg="#f8f8f8").place(x=420, y=105, width=320, height=30)

        # Row 2
        Label(self.reg_win, text="Contact No", font=("times new roman", 11, "bold"), bg="white").place(x=50, y=150)
        Entry(self.reg_win, textvariable=self.var_contact, font=("times new roman", 11), bg="#f8f8f8").place(x=50, y=175, width=320, height=30)

        Label(self.reg_win, text="Email", font=("times new roman", 11, "bold"), bg="white").place(x=420, y=150)
        Entry(self.reg_win, textvariable=self.var_email, font=("times new roman", 11), bg="#f8f8f8").place(x=420, y=175, width=320, height=30)

        # Row 3
        Label(self.reg_win, text="Select Security Questions", font=("times new roman", 11, "bold"), bg="white").place(x=50, y=220)
        combo_q = ttk.Combobox(self.reg_win, textvariable=self.var_security_q, font=("times new roman", 10), state="readonly")
        combo_q["values"] = ("Select", "Your Birth Place", "Your Pet Name", "Your Primary School")
        combo_q.current(0)
        combo_q.place(x=50, y=245, width=320, height=30)

        Label(self.reg_win, text="Security Answer", font=("times new roman", 11, "bold"), bg="white").place(x=420, y=220)
        Entry(self.reg_win, textvariable=self.var_security_a, font=("times new roman", 11), bg="#f8f8f8").place(x=420, y=245, width=320, height=30)

        # Row 4
        Label(self.reg_win, text="Password", font=("times new roman", 11, "bold"), bg="white").place(x=50, y=290)
        Entry(self.reg_win, textvariable=self.var_reg_pass, show="*", font=("times new roman", 11), bg="#f8f8f8").place(x=50, y=315, width=320, height=30)

        Label(self.reg_win, text="Confirm Password", font=("times new roman", 11, "bold"), bg="white").place(x=420, y=290)
        Entry(self.reg_win, textvariable=self.var_reg_cpass, show="*", font=("times new roman", 11), bg="#f8f8f8").place(x=420, y=315, width=320, height=30)

        # Checkbox
        Checkbutton(
            self.reg_win,
            text="I Agree The Terms & Conditions",
            variable=self.var_check,
            onvalue=1,
            offvalue=0,
            bg="white",
            font=("times new roman", 10, "bold"),
        ).place(x=50, y=365)

        # Action Buttons
        btn_register = Button(
            self.reg_win,
            text="Register Now",
            command=self.register_data,
            font=("times new roman", 13, "bold"),
            bg="#c0392b",
            fg="white",
            cursor="hand2",
            bd=0,
        )
        btn_register.place(x=50, y=420, width=180, height=40)

        btn_login = Button(
            self.reg_win,
            text="Login Now",
            command=self.reg_win.destroy,
            font=("times new roman", 13, "bold"),
            bg="#2980b9",
            fg="white",
            cursor="hand2",
            bd=0,
        )
        btn_login.place(x=260, y=420, width=180, height=40)

    def register_data(self):
        if (
            self.var_fname.get() == ""
            or self.var_email.get() == ""
            or self.var_security_q.get() == "Select"
            or self.var_security_a.get() == ""
            or self.var_reg_pass.get() == ""
        ):
            messagebox.showerror("Error", "All fields are required!", parent=self.reg_win)
        elif self.var_reg_pass.get() != self.var_reg_cpass.get():
            messagebox.showerror("Error", "Password & Confirm Password do not match!", parent=self.reg_win)
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to Terms & Conditions!", parent=self.reg_win)
        else:
            try:
                with open(USER_DATA_FILE, "a", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow([
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_security_q.get(),
                        self.var_security_a.get(),
                        self.var_reg_pass.get(),
                    ])
                messagebox.showinfo("Success", "Registration Successful!", parent=self.reg_win)
                self.reg_win.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save user: {e}", parent=self.reg_win)

    # ================= Forgot Password Window =================
    def forgot_password_window(self):
        self.forgot_win = Toplevel(self.root)
        self.forgot_win.title("Forgot Password")
        self.forgot_win.geometry("480x450+500+180")
        self.forgot_win.configure(bg="white")
        self.forgot_win.grab_set()

        self.var_forgot_email = StringVar()
        self.var_forgot_q = StringVar()
        self.var_forgot_a = StringVar()
        self.var_new_pass = StringVar()

        Label(
            self.forgot_win,
            text="FORGOT PASSWORD",
            font=("times new roman", 18, "bold"),
            bg="white",
            fg="red",
        ).pack(side=TOP, pady=15)

        Label(self.forgot_win, text="Registered Email / Username", font=("times new roman", 11, "bold"), bg="white").place(x=40, y=70)
        Entry(self.forgot_win, textvariable=self.var_forgot_email, font=("times new roman", 11), bg="#f8f8f8").place(x=40, y=95, width=400, height=30)

        Label(self.forgot_win, text="Select Security Question", font=("times new roman", 11, "bold"), bg="white").place(x=40, y=140)
        combo_fq = ttk.Combobox(self.forgot_win, textvariable=self.var_forgot_q, font=("times new roman", 10), state="readonly")
        combo_fq["values"] = ("Select", "Your Birth Place", "Your Pet Name", "Your Primary School")
        combo_fq.current(0)
        combo_fq.place(x=40, y=165, width=400, height=30)

        Label(self.forgot_win, text="Security Answer", font=("times new roman", 11, "bold"), bg="white").place(x=40, y=210)
        Entry(self.forgot_win, textvariable=self.var_forgot_a, font=("times new roman", 11), bg="#f8f8f8").place(x=40, y=235, width=400, height=30)

        Label(self.forgot_win, text="New Password", font=("times new roman", 11, "bold"), bg="white").place(x=40, y=280)
        Entry(self.forgot_win, textvariable=self.var_new_pass, show="*", font=("times new roman", 11), bg="#f8f8f8").place(x=40, y=305, width=400, height=30)

        btn_reset = Button(
            self.forgot_win,
            text="Reset Password",
            command=self.reset_password_action,
            font=("times new roman", 12, "bold"),
            bg="darkblue",
            fg="white",
            cursor="hand2",
            bd=0,
        )
        btn_reset.place(x=140, y=365, width=200, height=35)

    def reset_password_action(self):
        email = self.var_forgot_email.get().strip()
        q = self.var_forgot_q.get()
        a = self.var_forgot_a.get().strip()
        new_pass = self.var_new_pass.get().strip()

        if email == "" or q == "Select" or a == "" or new_pass == "":
            messagebox.showerror("Error", "All fields are required!", parent=self.forgot_win)
            return

        rows = []
        updated = False
        try:
            with open(USER_DATA_FILE, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                header = next(reader, None)
                if header:
                    rows.append(header)
                for row in reader:
                    if row and (row[3] == email or row[0] == email) and row[4] == q and row[5] == a:
                        row[6] = new_pass  # Update Password
                        updated = True
                    rows.append(row)

            if updated:
                with open(USER_DATA_FILE, "w", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerows(rows)
                messagebox.showinfo("Success", "Password updated successfully! You can now log in.", parent=self.forgot_win)
                self.forgot_win.destroy()
            else:
                messagebox.showerror("Error", "Invalid Security Details or User not found!", parent=self.forgot_win)
        except Exception as e:
            messagebox.showerror("Error", f"Could not update password: {e}", parent=self.forgot_win)


if __name__ == "__main__":
    root = Tk()
    app = LoginWindow(root)
    root.mainloop()