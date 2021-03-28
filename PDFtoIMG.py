from pdf2image import convert_from_path

pdfs = r"application-pdf.pdf"
pages = convert_from_path(pdfs, 18)

i = 1
for page in pages:
    image_name = "Page_" + str(i) + ".jpg"
    page.save('./raw_images/'+image_name, "JPEG")
    i = i+1

