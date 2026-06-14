import requests
import time
from core.config import settings

class CloudTTS:
    def __init__(self):
        # Configuration des modèles TTS par langue
        self.models = {
            "dioula": "facebook/mms-tts-dyu",
            "moore": "facebook/mms-tts-mos",
            "fr": "facebook/mms-tts-fra",
            "en": "facebook/mms-tts-eng"
        }
        self.headers = {"Authorization": f"Bearer {settings.HUGGINGFACE_TOKEN}"}




    def synthesize(self, text: str, lang: str = "dioula") -> bytes:
        """Génère de l'audio à partir du texte via l'API Hugging Face."""
        if lang not in self.models:
            print(f"Langue '{lang}' non supportée pour le TTS. Utilisation de 'dioula' par défaut.")
            lang = "dioula"
            
        model_id = self.models[lang]
        api_url = f"https://api-inference.huggingface.co/models/{model_id}"
        
        max_retries = 3
        for attempt in range(max_retries):
            try:
                # L'API Inference de HF pour le TTS attend un json avec {"inputs": "texte"}
                payload = {"inputs": text}
                response = requests.post(api_url, headers=self.headers, json=payload)
                
                if response.status_code == 200:
                    # La réponse est le flux audio (généralement audio/flac)
                    return response.content
                elif response.status_code == 503:
                    print(f"Le modèle TTS {lang} ({model_id}) est en cours de chargement. Tentative {attempt + 1}/{max_retries}...")
                    time.sleep(15)
                else:
                    print(f"Erreur API Hugging Face TTS ({lang}): {response.status_code} - {response.text}")
                    return None
            except Exception as e:
                print(f"Erreur de connexion à l'API TTS pour {lang}: {str(e)}")
                return None
                
        print(f"Échec de la génération TTS {lang} après plusieurs tentatives.")
        return None

# Instance singleton
tts_service = CloudTTS()
