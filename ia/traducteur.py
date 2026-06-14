import requests
import time
from core.config import settings

class CloudTranslator:
    def __init__(self):
        self.model_id = "facebook/nllb-200-distilled-600M"
        self.api_url = f"https://api-inference.huggingface.co/models/{self.model_id}"
        self.headers = {"Authorization": f"Bearer {settings.HUGGINGFACE_TOKEN}"}
        
        # Mapping des langues internes vers les codes NLLB-200
        self.lang_map = {
            "moore": "mos_Latn",
            "dioula": "dyu_Latn",
            "fr": "fra_Latn",
            "en": "eng_Latn"
        }

    def translate(self, text: str, src_lang: str, tgt_lang: str) -> str:
        if not text or not text.strip():
            return ""
            
        nllb_src = self.lang_map.get(src_lang, "fra_Latn")
        nllb_tgt = self.lang_map.get(tgt_lang, "fra_Latn")
        
        # Si la langue source et cible sont identiques, on retourne le texte tel quel
        if nllb_src == nllb_tgt:
            return text

        payload = {
            "inputs": text,
            "parameters": {
                "src_lang": nllb_src,
                "tgt_lang": nllb_tgt
            }
        }
        
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = requests.post(self.api_url, headers=self.headers, json=payload)
                if response.status_code == 200:
                    result = response.json()
                    if isinstance(result, list) and len(result) > 0 and "translation_text" in result[0]:
                        return result[0]["translation_text"]
                    return str(result)
                elif response.status_code == 503:
                    print(f"Modèle de traduction en cours de chargement. Tentative {attempt+1}/{max_retries}...")
                    time.sleep(15)
                else:
                    print(f"Erreur Traduction: {response.status_code} - {response.text}")
                    return text # En cas d'erreur, renvoyer l'original par sécurité
            except Exception as e:
                print(f"Erreur de connexion API Traduction: {e}")
                return text
                
        return text

translator_service = CloudTranslator()
