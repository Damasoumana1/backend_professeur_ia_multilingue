from fastapi import APIRouter, UploadFile, File, HTTPException, Form
from fastapi.responses import Response
import tempfile
import os
from ia.whisper_stt import stt_service
from ia.cloud_tts import tts_service

router = APIRouter()

@router.post("/transcribe", summary="Transcrire un fichier audio (Mooré, Dioula, Français, Anglais)")
async def transcribe_audio(
    file: UploadFile = File(...),
    lang: str = Form("moore", description="Langue de l'audio: 'moore', 'dioula', 'fr', ou 'en'")
):
    """Reçoit un fichier audio et le transcrit avec le modèle Whisper correspondant à la langue."""
    if not file.filename:
        raise HTTPException(status_code=400, detail="Aucun fichier fourni")
        
    try:
        # Création d'un fichier temporaire pour sauvegarder l'audio reçu
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
            content = await file.read()
            temp_audio.write(content)
            temp_audio_path = temp_audio.name

        # Utilisation de notre service pour transcrire
        transcription = stt_service.transcribe(temp_audio_path, lang=lang)
        
        # Nettoyage du fichier temporaire
        os.remove(temp_audio_path)
        
        return {"text": transcription, "lang": lang}
        
    except Exception as e:
        # En cas d'erreur, s'assurer que le fichier temporaire est supprimé
        if 'temp_audio_path' in locals() and os.path.exists(temp_audio_path):
            os.remove(temp_audio_path)
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/synthesize", summary="Générer de l'audio à partir de texte (TTS Mooré, Dioula, Français, Anglais)")
async def synthesize_speech(
    text: str = Form(..., description="Texte à prononcer"),
    lang: str = Form("moore", description="Langue: 'moore', 'dioula', 'fr', ou 'en'")
):
    """Génère un fichier audio à partir d'un texte via le modèle Hugging Face."""
    if not text.strip():
        raise HTTPException(status_code=400, detail="Le texte ne peut pas être vide")
        
    audio_bytes = tts_service.synthesize(text, lang=lang)
    
    if not audio_bytes:
        raise HTTPException(status_code=500, detail="Échec de la génération audio via l'API TTS")
        
    # Retourne directement l'audio sous forme de flux
    return Response(content=audio_bytes, media_type="audio/flac")

# Importations supplémentaires pour la pipeline
import base64
from ia.traducteur import translator_service
from ia.llm_engine import llm_service

@router.post("/pipeline/voice_chat", summary="Pipeline complète (STT -> NLLB -> LLM -> NLLB -> TTS)")
async def voice_chat_pipeline(
    file: UploadFile = File(...),
    lang: str = Form("moore", description="Langue de l'apprenant: 'moore', 'dioula', 'fr', ou 'en'")
):
    """Orchestre la pipeline d'IA complète : écoute, traduit, réfléchit, traduit, et répond en audio."""
    if not file.filename:
        raise HTTPException(status_code=400, detail="Aucun fichier fourni")
        
    try:
        # 1. Sauvegarde temporaire de l'audio
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
            content = await file.read()
            temp_audio.write(content)
            temp_audio_path = temp_audio.name

        # 2. STT : Audio -> Texte Local
        original_text = stt_service.transcribe(temp_audio_path, lang=lang)
        os.remove(temp_audio_path)
        
        if not original_text or not original_text.strip():
            raise HTTPException(status_code=400, detail="Impossible de transcrire l'audio (silence ou erreur).")

        # 3. Traduction : Texte Local -> Français (sauf si déjà en français)
        french_query = original_text
        if lang != "fr":
            french_query = translator_service.translate(original_text, src_lang=lang, tgt_lang="fr")

        # 4. LLM : Français -> Réponse Pédagogique Français
        french_answer = llm_service.generate_response(french_query)

        # 5. Traduction : Réponse FR -> Réponse Locale (sauf si déjà en français)
        local_answer = french_answer
        if lang != "fr":
            local_answer = translator_service.translate(french_answer, src_lang="fr", tgt_lang=lang)

        # 6. TTS : Réponse Locale -> Audio Bytes
        audio_bytes = tts_service.synthesize(local_answer, lang=lang)
        
        if not audio_bytes:
            raise HTTPException(status_code=500, detail="Échec de la génération audio finale.")

        # Encodage de l'audio en base64 pour l'inclure dans un JSON avec les textes
        audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")

        return {
            "lang": lang,
            "pipeline": {
                "1_stt_original": original_text,
                "2_translation_to_fr": french_query,
                "3_llm_answer_fr": french_answer,
                "4_translation_to_local": local_answer
            },
            "audio_base64": audio_base64,
            "audio_mime_type": "audio/flac"
        }
        
    except Exception as e:
        if 'temp_audio_path' in locals() and os.path.exists(temp_audio_path):
            os.remove(temp_audio_path)
        raise HTTPException(status_code=500, detail=str(e))


