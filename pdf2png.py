# simple script to convert pdf file into separate png images

'''
Dependencies
=============
-> Upgrade pip
        pip install pip --upgrade
-> install wand
        pip install wand
-> install PyPDF2
        pip install pypdf2

(I think that's it. But, if you have any problems, install the following too!)
*installed them in previous trials*

-> install ImageMagick , Ghostscript  >>> .exe   32-bit
        GhostScript : http://downloads.ghostscript.com/public/
        ImageMagick : https://wiki.python.org/moin/ImageMagick

'''


'''
HOW to use
===========
-> call convert(p1 , p2)
        p1 is a str = file name without .pdf
        p2 is optional -> int = resolution in dpi required
-> you can import this module in any script as usual
        from pdf2png import convert

'''

import PyPDF2
from wand.image import Image
import io

def pdf_page_to_png(src_pdf, pagenum = 0, resolution = 72,):
    '''
    Returns specified PDF page as wand.image.Image png.
    :param PyPDF2.PdfFileReader src_pdf: PDF from which to take pages.
    :param int pagenum: Page number to take.
    :param int resolution: Resolution for resulting png in DPI.
    '''
    dst_pdf = PyPDF2.PdfFileWriter()
    dst_pdf.addPage(src_pdf.getPage(pagenum))

    pdf_bytes = io.BytesIO()
    dst_pdf.write(pdf_bytes)
    pdf_bytes.seek(0)

    img = Image(file = pdf_bytes, resolution = resolution)
    img.convert("png")

    return img


def convert(pdf_name,resolution=72):
    '''
    Saves each page from a specified PDF as a png image (pdf_name{page_index}.png)
    :param str pdf_name : PDF file name (in the same directory of this script)
    :param int resolution : resolution of the output png_s in DPI
    '''
    src_pdf = PyPDF2.PdfFileReader(open(pdf_name+'.pdf', "rb"))
    for i in range(src_pdf.getNumPages()):
        temp=pdf_page_to_png(src_pdf,i,resolution)
        temp.save(filename=pdf_name+str(i)+'.png')


# Example of converting exam.pdf located at the same direcory
# convert('exam')   # NOTE : default resolution is 72 dpi
