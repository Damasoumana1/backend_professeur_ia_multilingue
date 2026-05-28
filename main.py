from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings
from core.database import engine, Base
from middleware import cors, logging_middleware

# Import routers (placeholders – will be created later)
from routers import auth, users, apprenants, parents, enseignants, matieres, lecons, exercices, sessions, interactions, progressions, recommendations, skills, learning_paths, notifications, ai

app = FastAPI(title="Professeur IA Multilingue", version="0.1.0")

# CORS middleware (basic configuration)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(apprenants.router, prefix="/apprenants", tags=["apprenants"])
app.include_router(parents.router, prefix="/parents", tags=["parents"])
app.include_router(enseignants.router, prefix="/enseignants", tags=["enseignants"])
app.include_router(matieres.router, prefix="/matieres", tags=["matieres"])
app.include_router(lecons.router, prefix="/lecons", tags=["lecons"])
app.include_router(exercices.router, prefix="/exercices", tags=["exercices"])
app.include_router(sessions.router, prefix="/sessions", tags=["sessions"])
app.include_router(interactions.router, prefix="/interactions", tags=["interactions"])
app.include_router(progressions.router, prefix="/progressions", tags=["progressions"])
app.include_router(recommendations.router, prefix="/recommendations", tags=["recommendations"])
app.include_router(skills.router, prefix="/skills", tags=["skills"])
app.include_router(learning_paths.router, prefix="/learning_paths", tags=["learning_paths"])
app.include_router(notifications.router, prefix="/notifications", tags=["notifications"])
app.include_router(ai.router, prefix="/ai", tags=["ai"])

# Create database tables on startup (for dev only)
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Placeholder root endpoint
@app.get("/")
async def root():
    return {"message": "Professeur IA Multilingue API is running"}
