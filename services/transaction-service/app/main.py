from fastapi import FastAPI
from dotenv import load_dotenv
from app.routes.transactions import router as transaction_router

load_dotenv()

app = FastAPI(title="Transaction Service", version="1.0.0")

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "transaction-service"}

app.include_router(transaction_router, prefix="/transactions")