import requests
import time
from core.config import settings

class PedagogicalLLM:
    def __init__(self):
        self.model_id = "meta-llama/Meta-Llama-3-8B-Instruct"
        # HF Inference API supports chat completions via this endpoint:
        self.api_url = f"https://api-inference.huggingface.co/models/{self.model_id}/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {settings.HUGGINGFACE_TOKEN}",
            "Content-Type": "application/json"
        }
        self.system_prompt = (
            "Tu es un professeur d'école primaire bienveillant au Burkina Faso. "
            "L'élève te pose une question. Réponds de façon très simple, "
            "bienveillante et extrêmement concise (maximum 2 à 3 phrases claires). "
            "Tu parles toujours en français, même si la question originale "
            "était dans une autre langue africaine."
        )

    def generate_response(self, user_text: str) -> str:
        if not user_text or not user_text.strip():
            return "Je n'ai pas bien entendu, peux-tu répéter ta question ?"

        payload = {
            "model": self.model_id,
            "messages": [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": user_text}
            ],
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = requests.post(self.api_url, headers=self.headers, json=payload)
                if response.status_code == 200:
                    result = response.json()
                    if "choices" in result and len(result["choices"]) > 0:
                        return result["choices"][0]["message"]["content"].strip()
                    return str(result)
                elif response.status_code == 503:
                    print(f"Modèle LLM en cours de chargement. Tentative {attempt+1}/{max_retries}...")
                    time.sleep(15)
                else:
                    # Fallback sur l'API standard si v1/chat/completions échoue ou n'est pas supporté
                    return self._fallback_generate(user_text)
            except Exception as e:
                print(f"Erreur de connexion API LLM: {e}")
                return "Désolé, je rencontre des difficultés techniques pour te répondre."
                
        return "Désolé, le cerveau du professeur met trop de temps à réfléchir."

    def _fallback_generate(self, user_text: str) -> str:
        fallback_url = f"https://api-inference.huggingface.co/models/{self.model_id}"
        prompt = f"<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n{self.system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>\n{user_text}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n"
        
        payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": 150,
                "temperature": 0.7,
                "return_full_text": False
            }
        }
        try:
            response = requests.post(fallback_url, headers=self.headers, json=payload)
            if response.status_code == 200:
                result = response.json()
                if isinstance(result, list) and len(result) > 0 and "generated_text" in result[0]:
                    return result[0]["generated_text"].strip()
            print(f"Erreur Fallback LLM: {response.status_code} - {response.text}")
        except Exception as e:
            pass
        return "Désolé, je n'arrive pas à formuler ma réponse."

llm_service = PedagogicalLLM()
