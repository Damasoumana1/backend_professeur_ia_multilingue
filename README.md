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

*   **Framework API :** [FastAPI](https://fastapi.tiangolo.com/) avec documentation Swagger UI intégrée
*   **Base de données :** PostgreSQL 15+ (via SQLAlchemy 2.0 async & asyncpg)
*   **Migrations :** Alembic
*   **Gestion des tâches :** Celery (pour les traitements audio lourds)
*   **IA & NLP :** LangChain, Whisper, Llama 3 / Mistral, gTTS

## 📁 Architecture du projet

L'architecture suit les meilleures pratiques Domain-Driven Design (DDD) :

```text
├── alembic/            # Migrations de base de données
├── core/               # Configuration (DB, Sécurité, Variables d'environnement)
├── models/             # Modèles SQLAlchemy (schéma de la base — 22 tables)
├── schemas/            # Modèles Pydantic (validation des entrées/sorties)
├── repositories/       # Couche d'accès aux données (CRUD)
├── services/           # Logique métier et orchestration
├── routers/            # Contrôleurs FastAPI (Endpoints)
├── ia/                 # Intégrations des modèles IA (Whisper, LLM, TTS, SE)
├── middleware/         # Middlewares (CORS, Rate Limiting, Auth)
├── tasks/              # Tâches asynchrones (Celery)
└── utils/              # Fonctions utilitaires diverses
```

## 📖 Documentation API (Swagger)

FastAPI génère automatiquement une documentation interactive de l'API.  
Une fois le serveur lancé, deux interfaces sont disponibles :

| Interface | URL | Description |
|-----------|-----|-------------|
| **Swagger UI** | `http://localhost:8000/docs` | Interface interactive pour tester les endpoints |
| **ReDoc** | `http://localhost:8000/redoc` | Documentation lisible et bien formatée |
| **OpenAPI JSON** | `http://localhost:8000/openapi.json` | Schéma brut (pour générer des clients) |

> **Tip :** Sur la page `/docs`, cliquez sur **Authorize 🔒** et entrez votre token JWT (obtenu via `POST /auth/login`) pour tester les endpoints protégés.

### Groupes d'endpoints disponibles

| Tag | Préfixe | Description |
|-----|---------|-------------|
| `auth` | `/auth` | Connexion, inscription, refresh token |
| `utilisateurs` | `/users` | CRUD des comptes utilisateurs |
| `apprenants` | `/apprenants` | Profils et scores des élèves |
| `parents` | `/parents` | Comptes parents et suivi |
| `enseignants` | `/enseignants` | Comptes enseignants |
| `matieres` | `/matieres` | Référentiel des matières |
| `lecons` | `/lecons` | Leçons multilingues |
| `exercices` | `/exercices` | QCM, vrai/faux, oral... |
| `sessions` | `/sessions` | Sessions d'apprentissage |
| `interactions` | `/interactions` | Interactions vocales STT/LLM/TTS |
| `progressions` | `/progressions` | Suivi par leçon |
| `skills` | `/skills` | Compétences pédagogiques |
| `learning_paths` | `/learning_paths` | Parcours personnalisés IA |
| `recommendations` | `/recommendations` | Recommandations IA |
| `notifications` | `/notifications` | Alertes in-app |
| `ia` | `/ai` | Transcription, traduction, synthèse |

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
```bash
cp .env.example .env
# Editez .env avec vos identifiants PostgreSQL
```

Exemple de contenu `.env` :
```ini
APP_NAME="Professeur IA Multilingue"
DEBUG=True
POSTGRES_SERVER=localhost
POSTGRES_USER=postgres
POSTGRES_PASSWORD=votre_mot_de_passe
POSTGRES_DB=professeur_ia
POSTGRES_PORT=5432
```

### 6. Lancement de l'API
```bash
uvicorn main:app --reload
```

L'API sera accessible sur **`http://localhost:8000`**.  
La documentation Swagger sera disponible sur **`http://localhost:8000/docs`**.

## 🏗️ État d'avancement

| Couche | Statut |
|--------|--------|
| Structure du projet | ✅ Terminé |
| Base de données PostgreSQL (22 tables) | ✅ Terminé |
| Modèles SQLAlchemy (22 modèles) | ✅ Terminé |
| Configuration Swagger / OpenAPI | ✅ Terminé |
| Schemas Pydantic | 🔄 En cours |
| Repositories (CRUD) | ⏳ À faire |
| Services (Logique métier) | ⏳ À faire |
| Routers (Endpoints API) | ⏳ À faire |
| Intégration Whisper (STT) | ⏳ À faire |
| Intégration LLM (Llama3/Mistral) | ⏳ À faire |
| Synthèse vocale (gTTS) | ⏳ À faire |

---
*Ce projet est réalisé dans le cadre d'un Master en Intelligence Artificielle appliquée au contexte africain.*
