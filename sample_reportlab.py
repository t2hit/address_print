from reportlab.pdfgen import canvas

c = canvas.Canvas("output_file/hello.pdf")
c.setFont("Courier", 80)
c.drawString(150, 150, "Hello World")
c.showPage()
c.drawString(150, 150, "Hello World")
c.showPage()
c.save()
