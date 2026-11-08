from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(title="Sentiment API")

# Загружаем модель один раз при старте приложения
classifier = pipeline(
    "text-classification",
    model="Facececersek/bedrock-sentiment-tiny"
)


class TextRequest(BaseModel):
    text: str


@app.get("/health")
def health():
    """Health check для Render."""
    return {"status": "ok"}


@app.post("/predict")
def predict(request: TextRequest):
    """Классифицирует тональность текста (positive / negative)."""
    result = classifier(request.text)[0]
    return {
        "label": result["label"],
        "score": round(result["score"], 4)
    }