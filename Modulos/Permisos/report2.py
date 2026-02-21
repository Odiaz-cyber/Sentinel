#! /usr/bin/python3
import reportlab 
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4 , letter
from reportlab.lib.utils import ImageReader

class Report:

    def __init__(self,name):
        self.name = name 

    def report(self):

        w , h = A4 # Ancho - Atura de A4 

        c = canvas.Canvas(self.name , pagesize=A4)

        img = ImageReader("recursos/sentinel.png")
        img_w , img_h = img.getSize()
           
        c.drawImage(img, 30, h - 200 , width=70 , height=70)

        c.save()







img = Report("report2.pdf")
img.report()