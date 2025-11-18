from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.router import api_router

origins = ["http://localhost:4200", "http://127.0.0.1:4200"]

app = FastAPI(title="Data Domain Portal API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/health", tags=["Monitoring"])
def health_check():
    return {"status": "ok"}
