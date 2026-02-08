# Tech Santa - AI Opportunity Compass 🎅💡

Tech Santa helps users identify solvable problems using AI. It analyzes problem descriptions, categorizes them, and provides technical guidance for potential solutions.

## Architecture

- **Frontend**: Streamlit (Python)
- **Backend**: FastAPI (Python)
- **Database**: MongoDB
- **AI**: Google Gemini Pro & ElevenLabs (Audio)

## Prerequisites

- [Docker](https://www.docker.com/) & Docker Compose
- *Or* Python 3.9+ and a MongoDB instance (local or Atlas)

## Quick Start (Docker) - Recommended

1.  **Clone the repository**
    ```bash
    git clone <repo-url>
    cd Tech-Santa
    ```

2.  **Environment Setup**
    Copy `.env.example` to `.env` and fill in your API keys.
    ```bash
    cp .env.example .env
    # Edit .env and add GEMINI_API_KEY
    ```

3.  **Run with Docker Compose**
    ```bash
    docker-compose up --build
    ```

4.  **Access the App**
    - Frontend: [http://localhost:8501](http://localhost:8501)
    - Backend API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

## Local Development Setup

If you prefer running services individually:

### 1. Database
Ensure you have a MongoDB instance running locally on port 27017, or update `MONGO_URI` in `.env`.

### 2. Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
pip install -r requirements.txt

# Run server
uvicorn main:app --reload
```

### 3. Frontend
```bash
cd frontend
# (Optional) Create a separate venv or use the same one if packages don't conflict, 
# but best practice suggests separate environments.
pip install -r requirements.txt

# Run Streamlit
streamlit run app.py
```

## Project Structure

```
.
├── backend/            # FastAPI application
│   ├── ai_service.py   # Gemini & ElevenLabs logic
│   ├── db.py           # Database connection
│   └── main.py         # API Endpoints
├── frontend/           # Streamlit application
│   └── app.py          # UI Logic
└── docker-compose.yml  # Orchestration
```

## Production Notes

- **Model Selection**: The system attempts to use `gemini-1.5-flash` or falls back to available models.
- **Security**: In a real production environment, ensure MongoDB authentication is enabled and API keys are managed via secure secrets management (not plain text .env in repo).
