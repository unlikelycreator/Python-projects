import tkinter as tk
from tkinter import filedialog
from tkinter import Text
import os
root = tk.Tk()
root.configure(background='black')
apps = []
if os.path.isfile('save.txt'):
	with open('save.txt', 'r') as f:
		tempApps = f.read()
		tempApps=tempApps.split(',')
		apps = [x for x in tempApps if x.strip()]


def addApps():
	for widget in frame.winfo_children():
		widget.destroy()
	filename = filedialog.askopenfilename(initialdir="/", title="select file", filetypes=(("executables", "*.exe"), ("all files", "*.*")))
	apps.append(filename)
	print(filename)


	for app in apps:
		label = tk.Label(frame, text=app, bg="black")
		label.pack()


def runapps():
	for app in apps:
		os.startfile(app)


canvas = tk.Canvas(root, height=700, width=700, bg="#6d7993")
canvas.pack()
frame = tk.Frame(root,bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
openfile = tk.Button(root, text="add Apps", padx=10, pady=5, fg="white", bg="#373737", command=addApps)
openfile.pack()
runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#373737", command=runapps)
runApps.pack()
for app in apps:
	Label = tk.Label(frame, text=app)
	Label.pack()
root.mainloop()


with open('save.txt', 'w') as f:
	for app in apps:
		f.write(app + ',')