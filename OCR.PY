'''
from PIL import Image
import
pytesseract 
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
import cv2
img = cv2.imread('cinza.jpg',0)
edges = cv2.Canny(img,100,200)
img_new = Image.fromarray(edges)
text = pytesseract.image_to_string(img_new, lang='eng')
print (text)
'''

'''
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
import numpy as np
import cv2

from PIL import Image

# tipando a leitura para os canais de ordem RGB
imagem = Image.open('cinza.jpg').convert('RGB')

# convertendo em um array editável de numpy[x, y, CANALS]
npimagem = np.asarray(imagem).astype(np.uint8)  

# diminuição dos ruidos antes da binarização
npimagem[:, :, 0] = 0 # zerando o canal R (RED)
npimagem[:, :, 2] = 0 # zerando o canal B (BLUE)

# atribuição em escala de cinza
im = cv2.cvtColor(npimagem, cv2.COLOR_RGB2GRAY) 

# aplicação da truncagem binária para a intensidade
# pixels de intensidade de cor abaixo de 127 serão convertidos para 0 (PRETO)
# pixels de intensidade de cor acima de 127 serão convertidos para 255 (BRANCO)
# A atrubição do THRESH_OTSU incrementa uma análise inteligente dos nivels de truncagem
ret, thresh = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) 

# reconvertendo o retorno do threshold em um objeto do tipo PIL.Image
binimagem = Image.fromarray(thresh) 

# chamada ao tesseract OCR por meio de seu wrapper
phrase = pytesseract.image_to_string(binimagem, lang='por')

# impressão do resultado
print(phrase)
'''

'''
import pytesseract

from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
custom_config = r'--oem 3 --psm 6 outputbase digits'
phrase = pytesseract.image_to_string(Image.open('cinza.jpg'),config=custom_config , lang='por' )
print(phrase)
'''


'''
from PIL import Image # Importando o módulo Pillow para abrir a imagem no script

import pytesseract # Módulo para a utilização da tecnologia OCR
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

print(pytesseract.image_to_string(Image.open('cinza.jpg'))) # Extraindo o texto da imagem
'''

'''
try:
    import pytesseract
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    print("deu certo")
except:
    print("erro aqui")
from PIL import Image
import cv2
import os

if __name__ == "__main__":
    
    #carrega a imagem colorida
    imagem = cv2.imread("cinza.jpg")
    
    #salva a imagem em um arquivo temporário do Windows para aplicar OCR
    filenameImagem = "{}.png".format(os.getpid())
    cv2.imwrite(filenameImagem, imagem)
    
    #carrega a imagem usando a biblioteca PIL/Pillow e aplica OCR
    texto = pytesseract.image_to_string(Image.open(filenameImagem))

    #deleta arquivo temporário
    os.remove(filenameImagem)
    
    print("Texto: " + texto)

    #redimensiona só pra ser exibido ao final
    imagem = cv2.resize(imagem,None,fx=0.25, fy=0.25, interpolation = cv2.INTER_CUBIC)

    #exibe a imagem
    cv2.imshow("imagem contendo o texto", imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
'''



'''
from PIL import Image
import pytesseract

#Include tesseract exe. path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# image object
image = Image.open('cinza.jpg')

#Pass image object to text

#text = pytesseract.image_to_string(image, lang='por')

#print(text)
print(pytesseract.run_and_get_output(image))
'''

'''
import cv2
import numpy as np

img = cv2.imread('cinza.jpg')

# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,5)
 
#thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#dilation
def dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
    
#erosion
def erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

#opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

#canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)

#skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

#template matching
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED) 
'''

'''
import base64
imgdata = base64.b64decode(imgstring)
filename = 'cinza.jpg'  # arquivo
with open(filename, 'wb') as f:
    f.write(imgdata)
'''

import os, io
from google.cloud import vision
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"ServiceAccountToken.json"

client = vision.ImageAnnotatorClient()

file_name = 'cinza.jpg'
image_path = f'.\VisionAPI\Images\{file_name}'

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

# construct an iamge instance
image = vision.types.Image(content=content)

"""
# or we can pass the image url
image = vision.types.Image()
image.source.image_uri = 'https://edu.pngfacts.com/uploads/1/1/3/2/11320972/grade-10-english_orig.png'
"""

# annotate Image Response
response = client.text_detection(image=image)  # returns TextAnnotation
df = pd.DataFrame(columns=['locale', 'description'])

texts = response.text_annotations
for text in texts:
    df = df.append(
        dict(
            locale=text.locale,
            description=text.description
        ),
        ignore_index=True
    )

print(df['description'][0])
