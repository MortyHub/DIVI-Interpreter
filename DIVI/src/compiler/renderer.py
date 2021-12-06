import tkinter as tk
from tkhtmlview import HTMLLabel

def startHTML(self, html, title, strip=True):
	root = tk.Tk()
	root.title(title)
	html_label = HTMLLabel(root, html=html)
	html_label.pack(fill="both", expand=True)
	html_label.fit_height()
	root.mainloop()




