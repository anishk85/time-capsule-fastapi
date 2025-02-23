from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
import warnings
import torch
import os
import uvicorn

# ✅ Suppress warnings
warnings.filterwarnings("ignore")
torch.set_printoptions(profile="none")

os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["TRANSFORMERS_VERBOSITY"] = "error"

# ✅ Load sentiment analysis model safely
classifier = None
try:
    classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")
except Exception as e:
    print(f"❌ Model Load Error: {str(e)}")
    classifier = None  # Allow API to run even if the model fails

# ✅ Define FastAPI app
app = FastAPI(title="Sentiment Analysis API", version="1.0")

# ✅ Request schema
class SentimentRequest(BaseModel):
    title: str
    message: str

# ✅ Sentiment classification function
def classify_text(text: str) -> str:
    if not classifier:
        raise HTTPException(status_code=500, detail="Model failed to load. Please try again later.")
    try:
        result = classifier(text)[0]
        return result["label"]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Classification Error: {str(e)}")

# ✅ API route for sentiment analysis
@app.post("/analyze")
async def analyze_sentiment(request: SentimentRequest):
    title_sentiment = classify_text(request.title)
    message_sentiment = classify_text(request.message)
    return {"title": title_sentiment, "message": message_sentiment}

# ✅ Root route
@app.get("/")
async def root():
    return {"message": "✅ Sentiment Analysis API is running!"}

# ✅ Ensure proper Uvicorn execution on Render
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  
    uvicorn.run(app, host="0.0.0.0", port=port)
