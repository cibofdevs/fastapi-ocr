from fastapi import FastAPI, File, UploadFile
import shutil
import pytesseract

app = FastAPI()

# set the tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


@app.post("/ocr")
def ocr(image: UploadFile = File(...)):
    file_path = 'txtFile'
    with open(file_path, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)
    return pytesseract.image_to_string(file_path, lang="eng")
