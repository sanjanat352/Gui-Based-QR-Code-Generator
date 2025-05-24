import qrcode
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Function to generate QR code
def generate_qr():
    data = entry.get()
    if not data:
        messagebox.showerror("Error", "Please enter some text or a URL!")
        return

    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Resize image and convert to PhotoImage for Tkinter
    img = img.resize((200, 200))
    img_tk = ImageTk.PhotoImage(img)

    # Display QR code
    qr_label.config(image=img_tk)
    qr_label.image = img_tk
    qr_label.qr_image = img  # Store original PIL image for saving

# Function to save QR code
def save_qr():
    if not hasattr(qr_label, "qr_image"):
        messagebox.showerror("Error", "No QR code generated!")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("All Files", "*.*")]
    )

    if file_path:
        qr_label.qr_image.save(file_path)
        messagebox.showinfo("Success", "QR Code saved successfully!")

# Create GUI window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x500")
root.resizable(False, False)

# Create widgets
tk.Label(root, text="Enter text or URL:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr,
                            font=("Arial", 12), bg="blue", fg="white")
generate_button.pack(pady=10)

save_button = tk.Button(root, text="Save QR Code", command=save_qr,
                        font=("Arial", 12), bg="green", fg="white")
save_button.pack(pady=5)

# QR Code Display Label
qr_label = tk.Label(root)
qr_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
