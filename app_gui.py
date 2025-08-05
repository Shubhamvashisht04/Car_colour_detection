import tkinter as tk
from tkinter import filedialog, Frame, Label
from PIL import Image, ImageTk
import cv2
import os

from detect_model import detect_objects
from color_check import is_blue_car

# --- Core Logic ---
def process_image(path):
    image, car_boxes, person_boxes = detect_objects(path)

    for box in car_boxes:
        if is_blue_car(image, box):
            color = (0, 0, 255)  # Red for blue car
        else:
            color = (255, 0, 0)  # Blue for other cars
        cv2.rectangle(image, (box[0], box[1]), (box[2], box[3]), color, 2)

    for box in person_boxes:
        cv2.rectangle(image, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)

    output_path = "output.jpg"
    cv2.imwrite(output_path, image)
    return output_path, len(car_boxes), len(person_boxes)

# --- Upload & Show Preview ---
def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
    if file_path:
        output_path, car_count, person_count = process_image(file_path)

        img = Image.open(output_path)
        img = img.resize((520, 400))
        img_tk = ImageTk.PhotoImage(img)

        preview_label.config(image=img_tk)
        preview_label.image = img_tk

        info_label.config(
            text=f"Cars Detected: {car_count}     People Detected: {person_count}",
            fg="#222"
        )

# --- GUI Setup ---
root = tk.Tk()
root.title("Car Colour Detection")
root.geometry("620x600")
root.configure(bg="#f1f3f4")
root.resizable(False, False)

# --- Header Frame ---
header = Frame(root, bg="#1f2937", height=60)
header.pack(fill="x")
title = Label(header, text="Car Colour Detection System", font=("Helvetica", 18, "bold"), bg="#1f2937", fg="white")
title.pack(pady=10)

# --- Upload Button ---
upload_btn = tk.Button(
    root, text="Upload Image", command=upload_image,
    font=("Segoe UI", 12), bg="#007bff", fg="white",
    activebackground="#0056b3", padx=20, pady=10, relief="flat", bd=0
)
upload_btn.pack(pady=20)

# --- Image Preview Area ---
preview_label = tk.Label(root, bd=3, relief="solid", width=520, height=400, bg="white")
preview_label.pack(pady=10)

# --- Info Display ---
info_label = tk.Label(root, text="", font=("Segoe UI", 13), bg="#f1f3f4")
info_label.pack(pady=10)

root.mainloop()
