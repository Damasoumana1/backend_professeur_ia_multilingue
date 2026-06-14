import requests
import time
from core.config import settings

class CloudSTT:
    def __init__(self):
        # Configuration des modèles par langue
        self.models = {
            "moore": "Dama12/whisper-small-moore",
            "dioula": "sudoping01/bambara-asr-v2",
            "fr": "openai/whisper-small",
            "en": "openai/whisper-small"
        }
        self.headers = {"Authorization": f"Bearer {settings.HUGGINGFACE_TOKEN}"}


    def transcribe(self, audio_file_path: str, lang: str = "moore") -> str:
        """Transcrit un fichier audio via l'API Hugging Face."""
        # Vérification de la langue
        if lang not in self.models:
            print(f"Langue '{lang}' non supportée. Utilisation de 'moore' par défaut.")
            lang = "moore"
            
        model_id = self.models[lang]
        api_url = f"https://api-inference.huggingface.co/models/{model_id}"
        
        try:
            with open(audio_file_path, "rb") as f:
                data = f.read()
        except FileNotFoundError:
            print(f"Erreur: Le fichier audio {audio_file_path} est introuvable.")
            return ""
            
        # L'API Hugging Face peut nécessiter un certain temps pour charger le modèle lors de la première requête
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = requests.post(api_url, headers=self.headers, data=data)
                
                if response.status_code == 200:
                    result = response.json()
                    # Selon l'API, le résultat peut être un dict ou une liste
                    if isinstance(result, dict) and "text" in result:
                        return result["text"]
                    elif isinstance(result, list) and len(result) > 0 and "text" in result[0]:
                        return result[0]["text"]
                    return str(result)
                elif response.status_code == 503:
                    # Modèle en cours de chargement sur l'API HF
                    print(f"Le modèle {lang} ({model_id}) est en cours de chargement. Tentative {attempt + 1}/{max_retries}...")
                    time.sleep(15)  # Attendre 15 secondes avant de réessayer
                else:
                    print(f"Erreur API Hugging Face ({lang}): {response.status_code} - {response.text}")
                    return ""
            except Exception as e:
                print(f"Erreur de connexion à l'API pour {lang}: {str(e)}")
                return ""
        
        print(f"Échec de la transcription {lang} après plusieurs tentatives (modèle trop long à charger).")
        return ""

# Instance singleton pour être réutilisée dans les différentes routes
stt_service = CloudSTT()
