# Intégration des Modèles IA (Pipeline Complète)

Ce document décrit l'architecture complète d'intégration des modèles d'Intelligence Artificielle au sein du projet **Professeur IA Multilingue**.

## 🚀 Approche Technique : L'API d'Inférence Hugging Face

Afin d'éviter le téléchargement de lourds modèles en local (gain de plus de 20 Go d'espace disque et d'utilisation de RAM/GPU), le backend utilise intégralement **l'API d'Inférence de Hugging Face**.

L'intelligence de l'application repose sur la synchronisation de 4 types d'IA différents, tous hébergés sur le Cloud et accessibles via un seul Token.

---

## 🎙️ 1. Reconnaissance Vocale (STT - Whisper)
Le service STT (`ia/whisper_stt.py`) "écoute" l'apprenant et convertit l'audio en texte.

| Langue | Modèle Hugging Face | Description |
|--------|---------------------|-------------|
| **Mooré** | [`Dama12/whisper-small-moore`](https://huggingface.co/Dama12/whisper-small-moore) | Modèle Whisper fine-tuné spécifiquement pour le Mooré. |
| **Dioula** | [`sudoping01/bambara-asr-v2`](https://huggingface.co/sudoping01/bambara-asr-v2) | Modèle ASR robuste pour le Dioula/Bambara. |
| **Français** | [`openai/whisper-small`](https://huggingface.co/openai/whisper-small) | Modèle multilingue universel natif. |
| **Anglais** | [`openai/whisper-small`](https://huggingface.co/openai/whisper-small) | Modèle multilingue universel natif. |

---

## 🌍 2. Traduction (NLLB-200)
Le service de traduction (`ia/traducteur.py`) permet de traduire les requêtes locales vers le français (pour qu'elles soient comprises par le cerveau LLM), et de traduire la réponse française vers la langue locale.

| Rôle | Modèle Hugging Face | Description |
|------|---------------------|-------------|
| **Traducteur** | [`facebook/nllb-200-distilled-600M`](https://huggingface.co/facebook/nllb-200-distilled-600M) | Modèle de Meta spécialisé dans 200 langues, dont les langues africaines peu dotées (`mos_Latn` pour le Mooré, `dyu_Latn` pour le Dioula). |

---

## 🧠 3. Moteur Pédagogique (LLM)
Le "cerveau" de l'application (`ia/llm_engine.py`) lit les questions en français et génère une réponse pédagogique.

| Rôle | Modèle Hugging Face | Description |
|------|---------------------|-------------|
| **Professeur IA** | [`meta-llama/Meta-Llama-3-8B-Instruct`](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) | LLM Open-Source surpuissant configuré avec un System Prompt le forçant à agir comme un enseignant de primaire au Burkina Faso (réponses bienveillantes et concises). |

---

## 🔊 4. Synthèse Vocale (TTS - MMS)
Le service TTS (`ia/cloud_tts.py`) convertit la réponse finale textuelle de l'IA en voix.

| Langue | Modèle Hugging Face | Description |
|--------|---------------------|-------------|
| **Mooré** | [`facebook/mms-tts-mos`](https://huggingface.co/facebook/mms-tts-mos) | Modèle ouvert de Meta (MMS) pour le Mooré. |
| **Dioula** | [`facebook/mms-tts-dyu`](https://huggingface.co/facebook/mms-tts-dyu) | Modèle ouvert de Meta (MMS) pour le Dioula. |
| **Français** | [`facebook/mms-tts-fra`](https://huggingface.co/facebook/mms-tts-fra) | Modèle ouvert de Meta (MMS) pour le Français. |
| **Anglais** | [`facebook/mms-tts-eng`](https://huggingface.co/facebook/mms-tts-eng) | Modèle ouvert de Meta (MMS) pour l'Anglais. |

---

## 💻 Orchestration & Endpoints (`routers/ai.py`)

L'application expose un "Super-Endpoint" qui enchaîne de façon asynchrone tous ces modèles :

### 🌟 La Route Principale : `POST /pipeline/voice_chat`
- **Entrée** : Fichier audio (`file`) et langue (`lang` : "moore", "dioula", "fr" ou "en").
- **Flux (Pipeline Pédagogique)** :
  1. **STT** (Audio Local -> Texte Local)
  2. **NLLB** (Texte Local -> Texte Français)
  3. **Llama-3** (Texte Français -> Réponse Pédagogique Français)
  4. **NLLB** (Réponse FR -> Réponse Locale)
  5. **TTS** (Réponse Locale -> Audio Local)
- **Sortie** : JSON contenant tous les textes des étapes intermédiaires ET l'audio final encodé en **Base64**.

### Routes Utilitaires (Modulaires)
- `POST /transcribe` : Pour utiliser uniquement le module de dictée/STT.
- `POST /synthesize` : Pour générer de l'audio TTS à partir d'une simple chaîne de caractères.

---

## 🔧 Authentification & Configuration
Toutes les requêtes vers l'API d'Inférence s'authentifient silencieusement via la clé d'API définie dans votre fichier `.env` :
```env
HUGGINGFACE_TOKEN="hf_votre_token_ici"
```
