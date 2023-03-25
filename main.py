import tkinter as tk
import tkinter.filedialog as filedialog

class TextEditor:
    def __init__(self, master):
        self.master = master
        master.title("Criação do arquivo CSV Tanita")

        # Create label with 300-character text
        label_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed quis metus ut ex laoreet malesuada. Morbi tempor fermentum urna eu consectetur. Sed et dolor blandit, vulputate augue ac, malesuada odio. Fusce non nisl vitae ipsum malesuada dapibus. Nullam non maximus purus, in commodo nulla. Vivamus euismod placerat faucibus. Integer sit amet justo blandit, consequat arcu non, vulputate elit. Duis ultrices hendrerit mauris sit amet fringilla. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec tristique mi at tellus vestibulum, at dictum dui pretium. Suspendisse a commodo ipsum. Nulla id ultrices tortor. Maecenas ac est justo."
        self.label = tk.Label(master, text=label_text, wraplength=580)

        self.label.pack(fill="both", expand=True)

        # Create text area
        self.text_area = tk.Text(master)
        self.text_area.pack()

        # Create submit button
        self.submit_button = tk.Button(master, text="Submit", command=self.submit_text)
        self.submit_button.pack()

    def submit_text(self):
        # Get text from text area and capitalize it
        text = self.text_area.get("1.0", "end-1c")
        capitalized_text = text.upper()

        # Ask user for file name and location
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")

        # Save capitalized text to file
        with open(file_path, "w") as file:
            file.write(capitalized_text)

# Create Tkinter window
root = tk.Tk()
root.geometry("600x500")
# Create TextEditor object
text_editor = TextEditor(root)

# Run the Tkinter event loop
root.mainloop()
