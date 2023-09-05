from pytesseract import image_to_string
from PIL import Image
from time import sleep
from pyautogui import write

try:
    image_path = "ss.png"
    image = Image.open(image_path)
    text = image_to_string(image)
    sleep(3)
    new=text.replace('\n',' ')
    for char in new:
        write(char)
except:
    print("Error !!!!!!")
    print("The screenshot was not found")
    print("Make sure you saved the screenshot with name 'ss' and it has .png extension")