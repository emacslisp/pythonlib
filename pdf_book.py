import PyPDF2

f = open('wiki.pdf', 'rb')

pdf_reader = PyPDF2.PdfFileReader(f)

print(pdf_reader.numPages)

page_one = pdf_reader.getPage(0)

page_one_text = page_one.extractText()

print(page_one_text)

pdf_writer = PyPDF2.PdfFileWriter()

pdf_writer.addPage(page_one)

pdf_output = open('wiki2.pdf', "wb")
pdf_writer.write(pdf_output)
f.close()
pdf_output.close()

## extract all page text
f = open('wiki.pdf', 'rb')

pdf_text = []
pdf_reader = PyPDF2.PdfFileReader(f)

for num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(num)
    pdf_text.append(page.extractText())

print(pdf_text)