import pyttsx3
import PyPDF2
book = open('Dreams-From-My-Father-by-Barack-Obama-Excerpt.pdf', 'rb')
reader = PyPDF2.PdfFileReader(book)
print(reader.numPages)
speaker = pyttsx3.init()
page = reader.getPage(16)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()
book.close()