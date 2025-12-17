# utils/chatbot.py
# Module chatbot pour interroger les donnees en langage naturel

import pandas as pd
from litellm import completion
from dotenv import load_dotenv

load_dotenv()


class DataChatbot:
    """Chatbot pour interroger les donnees en langage naturel."""
    
    def __init__(self, df: pd.DataFrame, model: str = "claude-sonnet-4-5-20250929"):
        """
        Initialise le chatbot avec les donnees.
        
        Args:
            df: DataFrame a analyser
            model: Modele LLM a utiliser
        """
        self.df = df
        self.model = model
        self.context = self._build_context()
        self.history = []
    
    def _build_context(self) -> str:
        """
        Construit le contexte des donnees pour l'IA.
        
        Permet au chatbot de comprendre la structure des donnees.
        
        Returns:
            String avec les infos du dataset
        """
        sample = self.df.head(5).to_string()
        stats = self.df.describe().to_string()
        
        return f"""
Tu es un assistant data qui aide a analyser un dataset.

STRUCTURE DU DATASET :
- Colonnes : {list(self.df.columns)}
- Types : {self.df.dtypes.to_dict()}
- Nombre de lignes : {len(self.df)}

ECHANTILLON :
{sample}

STATISTIQUES :
{stats}

Tu peux :
1. Repondre a des questions sur les donnees
2. Proposer des analyses
3. Generer du code Python pour manipuler les donnees
4. Expliquer les tendances observees

Sois concis et precis dans tes reponses.
"""
    
    def chat(self, user_message: str) -> str:
        """
        Envoie un message au chatbot et retourne la reponse.
        
        Args:
            user_message: Question de l'utilisateur
        
        Returns:
            Reponse du chatbot
        """
        messages = [
            {"role": "system", "content": self.context}
        ]
        
        # Ajouter l'historique
        messages.extend(self.history)
        
        # Ajouter le nouveau message
        messages.append({"role": "user", "content": user_message})
        
        try:
            response = completion(
                model=self.model,
                messages=messages
            )
            
            assistant_message = response.choices[0].message.content
            
            # Mettre a jour l'historique
            self.history.append({"role": "user", "content": user_message})
            self.history.append({"role": "assistant", "content": assistant_message})
            
            # Limiter l'historique a 10 echanges
            if len(self.history) > 20:
                self.history = self.history[-20:]
            
            return assistant_message
            
        except Exception as e:
            return f"Erreur : {str(e)}"
    
    def reset(self):
        """Reinitialise l'historique de conversation."""
        self.history = []