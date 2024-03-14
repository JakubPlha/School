import webbrowser
from tkinter import * 

root = Tk()
root.title("vir")
root.geometry("500x200")

def google():
    webbrowser.open("https://www.youtube.com/channel/UCbO-vj_tiGM8ds_PZH3pOhQ")

mygoogle = Button(root, text = "stahnout vir", command=google).pack(pady=20)
root.mainloop()