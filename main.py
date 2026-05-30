"""
Professeur IA Multilingue — Backend FastAPI
Groupe 5 | Master Intelligence Artificielle
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from fastapi.openapi.utils import get_openapi

from core.config import settings

# ── Metadata des tags pour Swagger ─────────────────────────
tags_metadata = [
    {
        "name": "auth",
        "description": "Authentification et gestion des tokens JWT (connexion, inscription, rafraîchissement).",
    },
    {
        "name": "utilisateurs",
        "description": "Gestion des comptes utilisateurs (apprenants, parents, enseignants, admins).",
    },
    {
        "name": "apprenants",
        "description": "Profils des élèves : score global, niveau scolaire, historique des sessions.",
    },
    {
        "name": "parents",
        "description": "Comptes parents et liaison avec les apprenants suivis.",
    },
    {
        "name": "enseignants",
        "description": "Comptes enseignants, établissements et spécialités.",
    },
    {
        "name": "matieres",
        "description": "Référentiel des matières (Maths, Lecture, Sciences, etc.).",
    },
    {
        "name": "lecons",
        "description": "Leçons multilingues (Français, Mooré, Dioula), disponibilité hors-ligne.",
    },
    {
        "name": "exercices",
        "description": "Exercices QCM, vrai/faux, texte libre, association et oral.",
    },
    {
        "name": "sessions",
        "description": "Sessions d'apprentissage : durée, score, mode de connexion.",
    },
    {
        "name": "interactions",
        "description": "Interactions vocales (Whisper STT / LLM / gTTS) avec scores de confiance.",
    },
    {
        "name": "progressions",
        "description": "Suivi de la progression par leçon : pourcentage, meilleur score.",
    },
    {
        "name": "skills",
        "description": "Compétences pédagogiques et niveau de maîtrise par apprenant.",
    },
    {
        "name": "learning_paths",
        "description": "Parcours d'apprentissage personnalisés générés par le moteur IA.",
    },
    {
        "name": "recommendations",
        "description": "Recommandations IA : leçons, exercices, révisions et parcours ciblés.",
    },
    {
        "name": "notifications",
        "description": "Notifications in-app (progression, alertes, badges, rappels).",
    },
    {
        "name": "ia",
        "description": "Endpoints IA directs : transcription vocale, traduction, synthèse vocale, LLM.",
    },
]

# ── Application FastAPI ─────────────────────────────────────
app = FastAPI(
    title="Professeur IA Multilingue",
    description="""
## API Backend — Professeur IA Multilingue 🎓

Système éducatif intelligent pour les écoles primaires du **Burkina Faso**,
proposant un assistant pédagogique en **Français, Mooré et Dioula**.

### Fonctionnalités
- 🎙️ **Reconnaissance vocale** multilingue (Whisper)
- 🧠 **Réponses intelligentes** (Llama 3 / Mistral via LangChain)
- 🔊 **Synthèse vocale** adaptée (gTTS)
- 📚 **Parcours adaptatif** personnalisé par apprenant
- ⚡ **Mode hors-ligne** pour les zones à faible connectivité
- 👨‍👩‍👧 **Multi-acteurs** : apprenants, parents, enseignants

### Authentification
Utilisez le endpoint **POST /auth/login** pour obtenir un token JWT,
puis cliquez sur le bouton **Authorize** 🔒 ci-dessus pour l'utiliser.
    """,
    version="1.0.0",
    openapi_tags=tags_metadata,
    contact={
        "name": "Groupe 5 — Master IA Burkina Faso",
        "url": "https://github.com/Damasoumana1/backend_professeur_ia_multilingue",
    },
    license_info={
        "name": "MIT",
    },
    docs_url="/docs",       # Swagger UI
    redoc_url="/redoc",     # ReDoc (alternative)
    openapi_url="/openapi.json",
)

# ── CORS ────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # En production : remplacer par les domaines autorisés
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Routers ─────────────────────────────────────────────────
from routers import (
    auth, users, apprenants, parents, enseignants,
    matieres, lecons, exercices, sessions, interactions,
    progressions, recommendations, skills, learning_paths,
    notifications, ai
)

app.include_router(auth.router,            prefix="/auth",            tags=["auth"])
app.include_router(users.router,           prefix="/users",           tags=["utilisateurs"])
app.include_router(apprenants.router,      prefix="/apprenants",      tags=["apprenants"])
app.include_router(parents.router,         prefix="/parents",         tags=["parents"])
app.include_router(enseignants.router,     prefix="/enseignants",     tags=["enseignants"])
app.include_router(matieres.router,        prefix="/matieres",        tags=["matieres"])
app.include_router(lecons.router,          prefix="/lecons",          tags=["lecons"])
app.include_router(exercices.router,       prefix="/exercices",       tags=["exercices"])
app.include_router(sessions.router,        prefix="/sessions",        tags=["sessions"])
app.include_router(interactions.router,    prefix="/interactions",    tags=["interactions"])
app.include_router(progressions.router,    prefix="/progressions",    tags=["progressions"])
app.include_router(recommendations.router, prefix="/recommendations", tags=["recommendations"])
app.include_router(skills.router,          prefix="/skills",          tags=["skills"])
app.include_router(learning_paths.router,  prefix="/learning_paths",  tags=["learning_paths"])
app.include_router(notifications.router,   prefix="/notifications",   tags=["notifications"])
app.include_router(ai.router,              prefix="/ai",              tags=["ia"])

# ── Endpoints racine ────────────────────────────────────────
@app.get("/", tags=["health"], summary="Vérification de l'état de l'API")
async def root():
    """
    Endpoint de vérification : confirme que l'API est opérationnelle.
    """
    return {
        "status": "online",
        "app": settings.APP_NAME,
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc",
    }


@app.get("/health", tags=["health"], summary="Health Check")
async def health_check():
    """
    Endpoint de santé pour le monitoring et les sondes de déploiement.
    """
    return {"status": "healthy"}
