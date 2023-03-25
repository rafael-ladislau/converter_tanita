import tkinter as tk
from tkinter import filedialog, messagebox
import re
import csv
import datetime

headers = {
    'Weight kg': 'Weight (kg)',
    'BMI BMI': 'BMI',
    'Body fat %': 'Body Fat (%)',
    'Torso %': 'Body fat (%) - trunk',
    'Left arm %': 'Body fat (%) - left arm',
    'Right arm %': 'Body fat (%) - right arm',
    'Left leg %': 'Body fat (%) - left leg',
    'Right leg %': 'Body fat (%) - right leg',
    'Muscle mass kg': 'Muscle Mass (kg)',
    'Torso kg': 'Muscle mass - trunk',
    'Left arm kg': 'Muscle mass - left arm',
    'Right arm kg': 'Muscle mass - right arm',
    'Left leg kg': 'Muscle mass - left leg',
    'Right leg kg': 'Muscle mass - right leg',
    'Muscle quality MQ': 'Muscle Quality',
    'Left arm MQ': 'Muscle quality - left arm',
    'Right arm MQ': 'Muscle quality - right arm',
    'Left leg MQ': 'Muscle quality - left leg',
    'Right leg MQ': 'Muscle quality - right leg',
    'Body type': 'Physique Rating',
    'Bone mass kg': 'Bone Mass (kg)',
    'Visceral fat': 'Visc Fat',
    'BMR kcal': 'BMR (kcal)',
    'Metabolic age years': 'Metab Age',
    'Body water %': 'Body Water (%)'
}

def submit_text():
    text = text_area.get("1.0", "end-1c")  # get text from text area

    # Define a regular expression pattern to capture numbers after colon
    pattern = r'[^a-zA-Z]*(.+):\s*([\d,\.]+)\s*([%a-zA-z]*)'

    # Find all matches of the pattern in the text and store them in a dictionary
    matches = re.findall(pattern, text)
    if not matches:
        messagebox.showwarning("Texto inválido", "O texto colado não foi reconhecido como um resultado WhatsApp ou email da Tanita.")
    else:
        results = {}
        for match in matches:
            group_name = match[0]
            if match[2] != '':
                group_name = group_name + ' ' + match[2]
            value = float(match[1].replace('.', '').replace(',', '.'))
            results[headers[group_name]] = value

        results['Date'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        results['Muscle quality - trunk'] = '-'
        results['Heart rate'] = '-'

        filename = filedialog.asksaveasfilename(defaultextension=".csv", initialfile="resultado.csv")  # get filename from user
        if filename:
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=results.keys())
                writer.writeheader()
                writer.writerow(results)
        messagebox.showinfo('Sucesso', 'O arquivo foi salvo com sucesso!')

root = tk.Tk()

# get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# calculate window position
window_width = 600
window_height = 500
x_pos = (screen_width - window_width) // 2
y_pos = (screen_height - window_height) // 2

# set window geometry and title
root.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")
root.resizable(False, False)
root.configure(padx=10, pady=10)
root.title("Criação do arquivo CSV Tanita")

# Create a label with wrapped text
label_text = "Cole abaixo o resultado recebido por e-mail ou WhatsApp. Clique no botão \"Enviar\" para salvar o arquivo."
label = tk.Label(root, text=label_text, wraplength=580)
label.pack(fill="both", expand=True, pady=20)

# Create a frame to hold the text area and submit button
frame = tk.Frame(root)

# Create a label with 300 characters of text
# intro_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas eget ante faucibus, congue lorem vitae, pulvinar nibh. Etiam sed tellus tellus. Nullam commodo, massa eget dignissim mollis, ipsum nunc vestibulum mauris, ut commodo tortor velit vel elit. Donec tincidunt justo sit amet commodo fringilla. Duis fringilla nisl nec mi molestie commodo. Suspendisse tincidunt euismod neque, at scelerisque enim bibendum ac. Proin vel risus justo. Integer sit amet dolor non velit luctus molestie."

# intro_label = tk.Label(frame, text=intro_text, wraplength=580, justify="left")
# intro_label.pack(side="top")

# Create a text area and submit button
text_area = tk.Text(frame)
submit_button = tk.Button(frame, text="Enviar", command=submit_text)

# Pack the text area and submit button
text_area.pack(fill="both", expand=True)
submit_button.pack(side="bottom")

# Add an empty line below the submit button
tk.Label(frame, text="").pack()

# Pack the frame to fill the window
frame.pack(fill="both", expand=True)

root.mainloop()

