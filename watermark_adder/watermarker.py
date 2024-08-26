import tkinter as tk
from tkinter import filedialog, simpledialog
from PIL import Image, ImageTk, ImageDraw, ImageFont


class Watermarker:
    def __init__(self, root):
        self._root = root
        self._root.title("Watermark adder")

        self.img = None

        self.upload_button = tk.Button(root, text="Upload image", command=self._upload_image)
        self.upload_button.pack(pady=10)

        # Create and pack the watermark button
        self.watermark_button = tk.Button(root, text="Add watermark", command=self._add_watermark)
        self.watermark_button.pack(pady=10)

        # Create a label widget for displaying images
        self.image_label = tk.Label(root)
        self.image_label.pack(padx=10, pady=10)

    def _upload_image(self):
        # Open file dialog and select an image file
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
        )

        if file_path:
            # Load the image
            self.img = Image.open(file_path)

            # Resize the image to fit within a predefined max size
            self.img.thumbnail((400, 400))

            # Convert the Image object into a Tkinter PhotoImage object
            img_tk = ImageTk.PhotoImage(self.img)

            # Update the label with the new image
            self.image_label.config(image=img_tk)
            self.image_label.image = img_tk  # Keep a reference to avoid garbage collection

    def _add_watermark(self):
        if self.img is None:
            return

            # Ask the user for watermark text
        watermark_text = simpledialog.askstring("Input", "Enter watermark text:")

        if watermark_text:
            # Add watermark to the image
            draw = ImageDraw.Draw(self.img)
            width, height = self.img.size

            # Load a default font
            try:
                # Try to load a more readable font
                font = ImageFont.truetype("arial.ttf", 20)
            except IOError:
                # Default to a basic PIL font if truetype font is unavailable
                font = ImageFont.load_default()

            text_width = draw.textlength(watermark_text, font=font)
            text_height = font.size  # Assuming single line, height is roughly the font size

            # Position the watermark at the bottom right corner
            x = width - text_width - 10
            y = height - text_height - 10

            draw.text((x, y), watermark_text, font=font, fill=(0, 0, 0, 128))  # RGBA color with transparency

            # Convert the modified Image object into a Tkinter PhotoImage object
            img_tk = ImageTk.PhotoImage(self.img)

            # Update the label with the new watermarked image
            self.image_label.config(image=img_tk)
            self.image_label.image = img_tk  # Keep a reference to avoid garbage collection
