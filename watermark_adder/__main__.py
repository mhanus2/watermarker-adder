import tkinter as tk

from watermark_adder.watermarker import Watermarker

# Initialize the main window
root = tk.Tk()

# Create the application object
app = Watermarker(root)

# Start the Tkinter event loop
root.mainloop()