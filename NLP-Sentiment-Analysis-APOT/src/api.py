#api.py
from fastapi import FastAPI
from predict import analyze_sentiment

app = FastAPI()

@app.get("/predict/")
def predict(text: str):
    result = analyze_sentiment(text)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
