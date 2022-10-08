from tkinter import Scale
import pyqrcode
import png

link = input("Enter your Link : ")
qr_code = pyqrcode.create(link)


for i in link.split("/"):
    if i.endswith(".com") is True:
        a = i.split(".")[0]
qr_code.png(f"{a}.png",scale=5)