#pip install pdf2docx



from pdf2docx import Converter

pdf_file = "pdf_files_name.pdf"
docx_file = "docx_files_name.docx"

cv = Converter(pdf_file = pdf_file)
cv.convert(docx_filename = docx_file)
cv.close()