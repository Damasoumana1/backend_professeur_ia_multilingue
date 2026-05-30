# 🎓 Professeur IA Multilingue — Backend

Bienvenue sur le dépôt backend du projet **Professeur IA Multilingue**.  
Il s'agit de l'API de l'application éducative destinée aux écoles primaires du Burkina Faso, conçue par le **Groupe 5**. L'application propose un assistant pédagogique dopé à l'intelligence artificielle (IA) capable de comprendre et de parler **Français, Mooré et Dioula**.

Ce backend orchestre un pipeline intelligent et hybride :
1. **Système Expert (SE)** pour encoder les règles pédagogiques.
2. **Modèles d'Apprentissage (ML & LLM)** pour la transcription vocale, la compréhension, et la synthèse vocale.

## 🚀 Fonctionnalités Principales

*   **🎙️ Multilingue et Vocal :** Reconnaissance vocale (STT avec Whisper) et Synthèse vocale (TTS avec gTTS) en Français, Mooré et Dioula.
*   **🧠 IA Adaptative :** Génération de réponses et d'explications (Llama 3 / Mistral) avec ajustement automatique selon le niveau scolaire de l'enfant.
*   **📚 Recommandations Personnalisées :** Parcours d'apprentissage individualisé et évaluation continue des compétences (Skills).
*   **⚡ Mode Hors-Ligne :** Architecture pensée pour télécharger du contenu et des réponses pré-générées pour les environnements à connectivité limitée.
*   **👨‍👩‍👧‍👦 Multi-acteurs :** Espaces dédiés pour les apprenants (élèves), les parents (suivi des performances), et les enseignants.

## 🛠️ Stack Technique

*   **Framework API :** [FastAPI](https://fastapi.tiangolo.com/)
*   **Base de données :** PostgreSQL (via SQLAlchemy 2.0 & asyncpg)
*   **Migrations :** Alembic
*   **Gestion des tâches :** Celery (pour les traitements audio lourds)
*   **IA & NLP :** LangChain, Whisper, Llama 3 / Mistral, gTTS

## 📁 Architecture du projet

L'architecture suit les meilleures pratiques Domain-Driven Design (DDD) :

```text
├── alembic/            # Migrations de base de données
├── core/               # Configuration (DB, Sécurité, Variables d'environnement)
├── models/             # Modèles SQLAlchemy (schéma de la base)
├── schemas/            # Modèles Pydantic (validation des entrées/sorties)
├── repositories/       # Couche d'accès aux données (CRUD)
├── services/           # Logique métier et orchestration
├── routers/            # Contrôleurs FastAPI (Endpoints)
├── ia/                 # Intégrations des modèles IA (Whisper, LLM, TTS, SE)
├── middleware/         # Middlewares (CORS, Rate Limiting, Auth)
├── tasks/              # Tâches asynchrones (Celery)
└── utils/              # Fonctions utilitaires diverses
```

## ⚙️ Installation et Démarrage (Développement)

### 1. Prérequis
- Python 3.10 ou supérieur
- PostgreSQL 15+ (avec extension `pgcrypto`)
- FFmpeg (pour le traitement audio par Whisper)

### 2. Cloner le projet
```bash
git clone https://github.com/Damasoumana1/backend_professeur_ia_multilingue.git
cd backend_professeur_ia_multilingue
```

### 3. Environnement virtuel
Créez et activez un environnement virtuel :
```bash
python -m venv venv
# Sur Windows :
venv\Scripts\activate
# Sur Linux/Mac :
source venv/bin/activate
```

### 4. Dépendances
```bash
pip install -r requirements.txt
```

### 5. Variables d'environnement
Dupliquez le fichier d'exemple et configurez vos identifiants de base de données :
```bash
cp .env.example .env
```
*(N'oubliez pas de renseigner la chaîne de connexion PostgreSQL dans le `.env`)*

### 6. Lancement de l'API
```bash
uvicorn main:app --reload
```
L'API sera accessible sur `http://localhost:8000`. Vous pouvez consulter la documentation interactive Swagger sur `http://localhost:8000/docs`.

---
*Ce projet est réalisé dans le cadre d'un Master en Intelligence Artificielle appliquée au contexte africain.*
