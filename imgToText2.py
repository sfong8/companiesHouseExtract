import cv2
import pytesseract
from PIL import Image

filename = './raw_images/Page_11.jpg'
text = pytesseract.image_to_string(Image.open(filename))