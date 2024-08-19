import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
from rembg import remove
import os

def process_image(file_path, output_path, size=(100, 100)):
    # Open image file
    image = Image.open(file_path)
    
    # Remove background
    image = remove(image)
    
    # Crop the image (for simplicity, cropping to the center 50% of the image)
    width, height = image.size
    left = width * 0.25
    top = height * 0.25
    right = width * 0.75
    bottom = height * 0.75
    image = image.crop((left, top, right, bottom))
    
    # Resize image
    image = image.resize(size)
    
    # Save processed image
    image.save(output_path)

def select_files():
    file_paths = filedialog.askopenfilenames(
        title="Select Images",
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg")]
    )
    if not file_paths:
        return
    
    output_folder = filedialog.askdirectory(title="Select Output Folder")
    if not output_folder:
        return

    for file_path in file_paths:
        try:
            filename = os.path.basename(file_path)
            output_path = os.path.join(output_folder, filename)
            process_image(file_path, output_path)
        except Exception as e:
            messagebox.showerror("Error", f"Error processing file {file_path}: {e}")
    
    messagebox.showinfo("Success", "Images processed successfully!")

# GUI setup
root = tk.Tk()
root.title("Image Processor")
root.geometry("300x150")

btn_select_files = tk.Button(root, text="Select Images and Process", command=select_files)
btn_select_files.pack(pady=20)

root
