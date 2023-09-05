# Auto Text From Image

Auto Text From Image is a Python script that automatically extracts text from an image and types it out. This can be especially useful when you need to quickly input text from an image into your computer.

## Prerequisites

Before running this script, ensure that you have the following installed:

- [Python 3.x](https://www.python.org/downloads)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed and added to your system's PATH.
- Required Python libraries: `pytesseract`, `Pillow` (PIL), and `pyautogui`. You can install them using `pip`:

  ```bash
  pip3 install pytesseract pillow pyautogui
  ```
  
## Usage

1. **Save a screenshot** as `ss.png` in the same directory as this script. Ensure that the screenshot contains the text you want to extract.

2. **Run the script**:

   ```bash
   python3 auto_text_from_image.py
   ```
3. **Place the cursor** where you want the text to get typed
4. The script will open the image, extract the text, and type it out character by character.
   The typed text will be exactly the same as the text in the image.
6. **Note** The script only waits for 3 seconds for you to place the cursor in location
   else it may type where you ran script
7. **Enjoy** watching the script type for you

## Future Enhancements

While the current version of the script works effectively for its intended purpose, there are several potential enhancements and improvements that can be considered for future development:

- **Multilingual Support:** Enhance the script to handle text extraction from images containing multiple languages.

- **GUI Interface:** Create a graphical user interface (GUI) that simplifies the process of selecting and processing images.

- **Batch Processing:** Add the capability to process multiple images in a batch, ideal for automating text extraction from a collection of screenshots.

- **Advanced OCR Techniques:** Explore advanced Optical Character Recognition (OCR) techniques or libraries to improve accuracy, especially for challenging image conditions.

- **Configurable Output:** Allow users to specify the output format or destination for the extracted text.

- **Error Handling:** Implement more robust error handling and user-friendly error messages.

Your contributions and ideas are welcome! Feel free to open issues or pull requests to discuss and implement these enhancements.
