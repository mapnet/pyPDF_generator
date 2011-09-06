'''
Created on 30/08/2011

@author: map
'''
from reportlab.pdfgen import canvas
def hello(c):
    c.drawString(100,130,"Hello Poul, I am an autogenrated PDF file")
    c.drawString(100,100,"lorem ipsum")
c = canvas.Canvas("hello.pdf")
hello(c)
c.showPage()
c.save()    