from fastapi import FastAPI, File, UploadFile
from nsfw_detector import NSFWDetector

app = FastAPI()
detector = NSFWDetector()  # LOAD ON STARTUP

@app.post("/scan-image")
async def scan_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    result = detector.scan_bytes(image_bytes)
    return result
