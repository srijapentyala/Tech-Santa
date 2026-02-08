import datetime
import random
from db import db

def seed_data():
    print("Connecting to DB...")
    db.connect()
    database = db.get_db()
    
    # Optional: Clear existing data to avoid duplicates
    # database.problems.delete_many({}) 

    demo_problems = [
        {
            "original_text": "Farmers in my village struggle to identify crop diseases early. We have smartphones but no internet in the fields. We need a way to take a photo of a leaf and know if it's sick.",
            "analysis": {
                "category": "Solvable",
                "industry": "Agriculture",
                "summary": "Offline mobile app for crop disease identification via image analysis.",
                "guidance": "TensorFlow Lite for mobile edge computing, Flutter for UI.",
                "reasoning": "Clear problem statement with existing technological solutions (edge AI).",
                "is_public": True
            },
            "created_at": datetime.datetime.utcnow(),
            "audio_b64": None 
        },
        {
            "original_text": "There is so much food waste at our university cafeteria. We need a system to track what is being thrown away so the kitchen can adjust portion sizes.",
            "analysis": {
                "category": "Solvable",
                "industry": "Sustainability",
                "summary": "AI-powered food waste tracking system for cafeterias.",
                "guidance": "Computer Vision (YOLO) to classify waste on trays, dashboard for analytics.",
                "reasoning": "High impact, technical feasibility is high using varied object detection models.",
                "is_public": True
            },
            "created_at": datetime.datetime.utcnow(),
            "audio_b64": None
        },
        {
            "original_text": "I have trouble focusing on long video lectures. I wish there was a tool that could just give me the key points and quizzes from a recorded localized video.",
            "analysis": {
                "category": "Solvable",
                "industry": "Education",
                "summary": "Video lecture summarizer and quiz generator.",
                "guidance": "OpenAI Whisper for transcription, LLM for summarization/quiz generation.",
                "reasoning": "Standard NLP task, very solvable.",
                "is_public": True
            },
            "created_at": datetime.datetime.utcnow(),
            "audio_b64": None
        },
        {
            "original_text": "Small businesses in my town are getting scammed by fake digital invoices. They don't have IT teams to check them.",
            "analysis": {
                "category": "Solvable",
                "industry": "FinTech",
                "summary": "Automated digital invoice verification tool.",
                "guidance": "OCR for document reading, rules engine + ML for anomaly detection.",
                "reasoning": "Solvable fraud detection problem.",
                "is_public": True
            },
            "created_at": datetime.datetime.utcnow(),
            "audio_b64": None
        },
        {
            "original_text": "Potholes in my city are dangerous. I want to report them while driving without touching my phone.",
            "analysis": {
                "category": "Solvable",
                "industry": "Civic/Auto",
                "summary": "Voice-activated or dashcam-based pothole reporting system.",
                "guidance": "Voice API or Accelerometer data analysis from phone.",
                "reasoning": "Practical safety application with multiple solution paths.",
                "is_public": True
            },
            "created_at": datetime.datetime.utcnow(),
            "audio_b64": None
        }
    ]

    # Add metrics dynamically to each seeded item
    for p in demo_problems:
        p["metrics"] = {
            "likes": random.randint(10, 500),
            "views": random.randint(500, 2000),
            "difficulty": random.choice(["Low", "Medium", "High"]),
            "impact_score": random.randint(50, 100)
        }

    print(f"Seeding {len(demo_problems)} problems...")
    database.problems.insert_many(demo_problems)
    print("Database seeded successfully!")
    db.close()

if __name__ == "__main__":
    seed_data()
