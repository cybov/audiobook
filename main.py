import pyttsx3, PyPDF2  #Import necessary modules
book = open('oop.pdf', 'rb')  #Open pdf in read binary mode. "oop.pdf" can be changed to any desired book.  
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()  #Initialize device speaker
for num in range(7, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
