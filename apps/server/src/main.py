from fastapi import FastAPI

app = FastAPI(title="Data Domain Portal API")

@app.get("/health")
def health_check():
    return {"status": "ok"}
