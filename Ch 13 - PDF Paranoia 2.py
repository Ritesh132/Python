
import os
import PyPDF2
import re
import pprint

os.chdir(r'C:\Users\tomal\Desktop\pdfs')
path = os.getcwd()

pdf_list = []


for folder, subfolders, files in os.walk(path):
    for file in files:
        if file.endswith(('.pdf', '.PDF')):
            try:
                pdf = open(os.path.join(folder, file), 'rb')
                pdf_reader = PyPDF2.PdfFileReader(pdf)
                pdf_reader.getPage(0)
            except PyPDF2.utils.PdfReadError:
                try:
                    pdf = open(os.path.join(folder, file), 'rb')
                    print(os.path.join(folder, file))
                    pdf_reader = PyPDF2.PdfFileReader(pdf)
                    pdf_reader.decrypt('rosebud')
                    pdf_reader.getPage(0)
                    print('Decrypting %s...' % file)
                    pdf_writer = PyPDF2.PdfFileWriter()
                    for page_num in range(0, pdf_reader.numPages):
                        page_obj = pdf_reader.getPage(page_num)
                        pdf_writer.addPage(page_obj)
                    new_name = re.sub('_encrypted', '_decrypted', file)
                    new_pdf = open(os.path.join(folder, new_name), 'wb')
                    pdf_writer.write(new_pdf)
                    pdf.close()
                    new_pdf.close()
                    pdf_list.append(file)
                except PyPDF2.utils.PdfReadError:
                    print('Could not decrypt %s' % file)

print('Successfully decrypted the following:')
pprint.pprint(pdf_list)
