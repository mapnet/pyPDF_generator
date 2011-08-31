'''
Created on 30/08/2011

@author: map
'''
from reportlab.pdfgen import canvas
def hello(c):
    c.drawString(100,120,"Hello Stefan, I am an autogenrated PDF file")
    c.drawString(100,100,"Will you please show Mads how to use github")
c = canvas.Canvas("hello.pdf")
hello(c)
c.showPage()
c.save()    