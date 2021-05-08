from PyPDF2 import PdfFileMerger


merg= PdfFileMerger()

#pdf acma -->
#cokhos= open("cokhos.pdf","rb")
"""
merg.append("cokhos.pdf")
merg.append("cpe323msp430_ISA.pdf")

merg.write("birlescek.pdf")
"""

#3.sayfaya ekledik
merg.append("cokhos.pdf")
merg.merge(3,"cpe323msp430_ISA.pdf")
merg.write("birles1.pdf")



"""
0.indexe kayıt

merg.append("cokhos.pdf")
merg.merge(0,"cpe323msp430_ISA.pdf")
merg.write("birles.pdf")
"""