import os
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import cv2  # Requires: pip install opencv-contrib-python
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train Data - Face Recognition System")

        # ================= Main Title =================
        title_lbl = Label(
            self.root,
            text="TRAIN DATA SET",
            font=("Times New Roman", 35, "bold"),
            bg="white",
            fg="red"
        )
        title_lbl.place(x=0, y=0, width=1530, height=50)

        # ================= Top Banner Image =================
        img_top = Image.open(r"C:\Users\sudee\OneDrive\Desktop\DATA SCIENCE\face recognition\face_recognition\face2.jpg")
        img_top = img_top.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl_top = Label(self.root, image=self.photoimg_top)
        f_lbl_top.place(x=0, y=55, width=1530, height=325)

        # ================= Train Dataset Button =================
        btn_train = Button(
            self.root,
            text="TRAIN DATA",
            command=self.train_classifier,
            cursor="hand2",
            font=("Times New Roman", 25, "bold"),
            bg="red",
            fg="white"
        )
        btn_train.place(x=0, y=380, width=1530, height=60)

        # ================= Bottom Image =================
        img_bottom = Image.open(r"C:\Users\sudee\OneDrive\Desktop\DATA SCIENCE\face recognition\face_recognition\face3.jpg")
        img_bottom = img_bottom.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl_bottom = Label(self.root, image=self.photoimg_bottom)
        f_lbl_bottom.place(x=0, y=440, width=1530, height=325)

    # ================= Train Classifier Method =================
    def train_classifier(self):
        data_dir = "data"

        # 1. Check if 'data' folder exists
        if not os.path.exists(data_dir):
            messagebox.showerror(
                "Error",
                "No 'data' folder found in the project directory!\nPlease capture photo samples first.",
                parent=self.root
            )
            return

        # 2. Get list of valid image paths
        path = [
            os.path.join(data_dir, file) 
            for file in os.listdir(data_dir) 
            if file.lower().endswith(('.jpg', '.jpeg', '.png'))
        ]

        if len(path) == 0:
            messagebox.showerror(
                "Error",
                "No training images (.jpg / .png) found inside 'data' folder!",
                parent=self.root
            )
            return

        faces = []
        ids = []

        # 3. Read and convert images
        for image_path in path:
            try:
                # Convert image to Grayscale
                img = Image.open(image_path).convert('L')
                imageNp = np.array(img, 'uint8')

                # Extract Student ID safely from filename format: user.<Student_ID>.<Sample_Num>.jpg
                filename = os.path.basename(image_path)
                parts = filename.split('.')
                
                # Check if file follows the standard user.ID.Sample.jpg naming convention
                if len(parts) >= 3:
                    id_num = int(parts[1])
                    faces.append(imageNp)
                    ids.append(id_num)

                    # Live preview while training
                    cv2.imshow("Training Dataset in Progress...", imageNp)
                    cv2.waitKey(1)
            except Exception as e:
                continue

        cv2.destroyAllWindows()

        if len(faces) == 0:
            messagebox.showerror(
                "Error",
                "No valid images were parsed. Make sure images are named as: user.<ID>.<Sample>.jpg",
                parent=self.root
            )
            return

        ids = np.array(ids)

        # 4. Train LBPH Classifier with Compatibility Check
        try:
            # Standard opencv-contrib method
            clf = cv2.face.LBPHFaceRecognizer_create()
        except AttributeError:
            try:
                # Legacy opencv method fallback
                clf = cv2.face.LBPHFaceRecognizer()
            except AttributeError:
                messagebox.showerror(
                    "OpenCV Error",
                    "LBPH Face Recognizer module not found!\n\nPlease run:\npip install opencv-contrib-python",
                    parent=self.root
                )
                return

        # Execute Training and Save Classifier
        clf.train(faces, ids)
        clf.write("classifier.xml")

        messagebox.showinfo(
            "Success",
            f"Training dataset completed successfully!\nTrained {len(ids)} face samples into 'classifier.xml'.",
            parent=self.root) 

 





if __name__ == "__main__":
    root = Tk()
    app = Train(root)
    root.mainloop()   