import datetime

MOCK_OPPORTUNITIES = [
    {
        "_id": "mock_1",
        "original_text": "Farmers in my village struggle to identify crop diseases early. We have smartphones but no internet in the fields.",
        "metrics": {
            "likes": 124,
            "views": 450,
            "difficulty": "Medium", # Low, Medium, High
            "impact_score": 95
        },
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
        "_id": "mock_2",
        "original_text": "There is so much food waste at our university cafeteria. We need a system to track what is being thrown away.",
        "metrics": {
            "likes": 89,
            "views": 210,
            "difficulty": "High",
            "impact_score": 88
        },
        "analysis": {
            "category": "Solvable",
            "industry": "Sustainability",
            "summary": "AI-powered food waste tracking system for cafeterias.",
            "guidance": "Computer Vision (YOLO) to classify waste on trays, dashboard for analytics.",
            "reasoning": "High impact, technical feasibility is high.",
            "is_public": True
        },
        "created_at": datetime.datetime.utcnow(),
        "audio_b64": None
    },
    {
        "_id": "mock_3",
        "original_text": "Small businesses in my town are getting scammed by fake digital invoices.",
        "metrics": {
            "likes": 256,
            "views": 1020,
            "difficulty": "Medium",
            "impact_score": 92
        },
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
    }
]
