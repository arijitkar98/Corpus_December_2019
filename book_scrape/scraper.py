from PyPDF2 import PdfFileReader
 
 
def text_extractor(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)

        file = open("raw.txt",'a')
        # file = open("test.txt",'w')
        for i in range(21,532):
            page = pdf.getPage(i)
            text = page.extractText()
            file.write(text) 
            file.write("\n")

        file.close()
 
if __name__ == '__main__':
    path = '../../books/Computer Structures - Readings and Examples.pdf'
    text_extractor(path)
