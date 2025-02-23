from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
import warnings
import torch
import os

# ✅ Suppress warnings
warnings.filterwarnings("ignore")
torch.set_printoptions(profile="none")

os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["TRANSFORMERS_VERBOSITY"] = "error"

# ✅ Load sentiment analysis model
try:
    classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")
except Exception as e:
    raise RuntimeError(f"Model Load Error: {str(e)}")

# ✅ Define FastAPI app
app = FastAPI(title="Sentiment Analysis API", version="1.0")

# ✅ Request schema
class SentimentRequest(BaseModel):
    title: str
    message: str

# ✅ Sentiment classification function
def classify_text(text: str) -> str:
    try:
        result = classifier(text)[0]
        return result["label"]
    except Exception as e:
        return f"Classification Error: {str(e)}"

# ✅ API route for sentiment analysis
@app.post("/analyze")
async def analyze_sentiment(request: SentimentRequest):
    try:
        title_sentiment = classify_text(request.title)
        message_sentiment = classify_text(request.message)
        return {"title": title_sentiment, "message": message_sentiment}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ✅ Root route
@app.get("/")
async def root():
    return {"message": "Sentiment Analysis API is running 🚀"}
