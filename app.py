from fastapi import FastAPI, File, UploadFile, Header, HTTPException
from nsfw_detector import NSFWDetector
import os

app = FastAPI()
detector = NSFWDetector()  # LOAD ON STARTUP

AI_SECRET = os.environ.get("AI_SECRET", "default-key")

@app.post("/scan-image")
async def scan_image(
    file: UploadFile = File(...),
    x_ai_key: str = Header(None)
):
    # 🔒 Verify API key
    if x_ai_key != AI_SECRET:
        raise HTTPException(status_code=403, detail="Unauthorized")
    
    image_bytes = await file.read()
    result = detector.scan_bytes(image_bytes)
    return result
