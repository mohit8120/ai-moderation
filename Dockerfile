FROM python:3.9-slim

WORKDIR /app

# Upgrade pip + force fresh install (VERY IMPORTANT)
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

COPY . .

# Reduce TensorFlow log noise
ENV TF_CPP_MIN_LOG_LEVEL=2

# AI_SECRET injected by Railway
ENV AI_SECRET=${AI_SECRET}

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
