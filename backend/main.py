import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from contextlib import asynccontextmanager
from db import db
from ai_service import evaluate_problem, generate_audio_summary
from mock_data import MOCK_OPPORTUNITIES
from datetime import datetime
import base64
import uuid

MOCK_MODE = os.getenv("MOCK_MODE", "False").lower() == "true"

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    if not MOCK_MODE:
        db.connect()
    yield
    # Shutdown
    if not MOCK_MODE:
        db.close()

app = FastAPI(lifespan=lifespan)

class ProblemSubmission(BaseModel):
    description: str

@app.post("/submit")
async def submit_problem(submission: ProblemSubmission):
    # 1. AI Analysis
    analysis = evaluate_problem(submission.description)
    
    # 2. Store in DB
    document = {
        "original_text": submission.description,
        "analysis": analysis,
        "created_at": datetime.utcnow(),
        "audio_b64": None
    }
    
    # 3. Generate Audio only if it's a "Solvable" opportunity
    if analysis.get("is_public"):
        audio_bytes = generate_audio_summary(analysis.get("summary", "New opportunity available"))
        if audio_bytes:
            document["audio_b64"] = base64.b64encode(audio_bytes).decode('utf-8')

    if MOCK_MODE:
        # Simulate ID generation and return immediately
        return {"id": str(uuid.uuid4()), "status": "submitted (mock)", "analysis": analysis}

    database = db.get_db()
    result = database.problems.insert_one(document)
    
    return {"id": str(result.inserted_id), "status": "submitted", "analysis": analysis}

@app.get("/opportunities")
async def get_opportunities():
    if MOCK_MODE:
        return MOCK_OPPORTUNITIES

    database = db.get_db()
    # Fetch only public/solvable problems
    cursor = database.problems.find({"analysis.is_public": True}).sort("created_at", -1)
    
    results = []
    for doc in cursor:
        doc["_id"] = str(doc["_id"])
        results.append(doc)
        
    return results

@app.get("/")
def home():
    return {"message": "API is running"}
