img_list = ['Aclonica.png','Amatic sc.png','Arial.png','Calibri.png','Courier.png','Helvetica neue.png','Jua.png','Lobster.png','pattaya.png','Times New Roman.png']
list1 = ['Aclonica','Amatic sc','Arial','Calibri','Courier','Helvetica neue','Jua','Lobster','pattaya','Times New Roman']

import cv2
import pytesseract
i = 0
while i < len(img_list):
    input_dir = "/home/jija/Desktop/files/OCR imgtotxt/images/"+ img_list[i]
    img = cv2.imread(input_dir , 1)
    result = pytesseract.image_to_pdf_or_hocr(img,lang = "eng")
    f = open("/home/jija/Desktop/files/OCR imgtotxt/searchable_pdf/searchablePDF"+list1[i]+".pdf","w+b")
    f.write(bytearray(result))
    f.close()
    i+=1
