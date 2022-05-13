from fastapi import FastAPI

from transformers import pipeline
from pydantic import BaseModel

sentiment_model = pipeline("sentiment-analysis")

# sentiment_query_sentence = get_random_comment(top_comments)
# sentiment = sentiment_model(sentiment_query_sentence)
# print(f"Sentiment test: {sentiment_query_sentence} == {sentiment})

class PredictionRequest(BaseModel):
  query_string: str

app = FastAPI()

@app.get("/health")
def health():
    return "Service is online."

@app.post("/docs")
def my_endpoint(request: PredictionRequest):
  # YOUR CODE GOES HERE
  #print(request)
  result = sentiment_model(request.query_string)
  return {'sentiment': result}

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}