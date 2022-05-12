from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return "Service is online."

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}