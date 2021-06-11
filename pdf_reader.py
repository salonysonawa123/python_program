import PyPDF2
import pyttsx3
speaker = pyttsx3.init()
book = open("E:\pythonlearn.pdf","rb")
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
print(pages)
page = pdfreader.getPage(13)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()