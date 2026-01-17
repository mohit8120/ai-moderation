import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
from PIL import Image
import io

LABELS = ["neutral", "sexy", "porn", "hentai"]

_model = None  # GLOBAL MODEL

def get_model():
    global _model
    if _model is None:
        print("🔄 Loading NSFW model...")
        _model = tf.keras.models.load_model(
            "nsfw_model.h5",
            custom_objects={"KerasLayer": hub.KerasLayer},
            compile=False
        )
        print("✅ NSFW model loaded")
    return _model


def scan_bytes(image_bytes):
    model = get_model()

    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img = img.resize((224, 224))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    preds = model.predict(img)[0]
    result = dict(zip(LABELS, preds))

    nudity_score = result["porn"] + result["hentai"]

    return {
        "nudity_score": float(nudity_score),
        "details": result
    }
