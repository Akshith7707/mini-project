from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routes
from routes import resume

app = FastAPI()

# CORS enabled so frontend (React on port 3000) can talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all for dev (restrict in prod)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint (for testing connection)
@app.get("/")
def root():
    return {"message": "AI Interview Bot Backend Running 🚀"}

# Register resume upload route with prefix /resume
app.include_router(resume.router, prefix="/resume", tags=["Resume"])