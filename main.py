import PyPDF2 
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from pdfrw import PdfReader, PdfWriter


# Nome de entrada e saída
input_file = "teste1.pdf"
output_file = ("MODIFICADO " + input_file)

# O que será lido e escrito
reader_input = PdfReader(input_file)
writer_output = PdfWriter()

# Lê as páginas e seleciona a partir da 4 pra ir para o novo arquivo
for current_page in range(len(reader_input.pages)):
    if current_page > 2:
        writer_output.addpage(reader_input.pages[current_page])
        print("Adicionando a página %i" % (current_page + 1))

# Cria o novo arquivo
writer_output.write(output_file)

# Importa o arquivo que está na raiz junto ao script
filename = output_file
pdfFileObj = open(filename,'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
num_pages = pdfReader.numPages
count = 0
text = ""

while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()

if text != "":
   text = text
# Transforma o PDF em TXT
else:
   text = textract.process(fileurl, method='tesseract', language='por')



tokens = word_tokenize(text)
punctuations = ['(',')',';',':','[',']',',']
stop_words = stopwords.words('portuguese')
# Vetor com o texto convertido
keywords = [word for word in tokens if not word in stop_words and not word in punctuations]
# Mostra o vetor com as palavras filtradas
print(keywords)