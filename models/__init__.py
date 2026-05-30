# Expose all models for Alembic and SQLAlchemy
from .enums import RoleEnum, LangueEnum, TypeExerciceEnum, TypeInteractionEnum, ModeConnexionEnum

from .utilisateur import Utilisateur
from .apprenant import Apprenant
from .parent import Parent, parent_apprenant
from .enseignant import Enseignant

from .matiere import Matiere
from .lecon import Lecon
from .exercice import Exercice
from .contenu_offline import ContenuOffline

from .session import SessionApprentissage
from .reponse import ReponseExercice
from .progression import ProgressionLecon
from .profil_linguistique import ProfilLinguistique
from .interaction_vocale import InteractionVocale

from .ai_model import AIModel
from .prompt_template import PromptTemplate
from .skill import Skill
from .student_skill import StudentSkill
from .learning_path import LearningPath, LearningPathLecon
from .recommendation import Recommendation
from .voice_dataset import VoiceDataset
from .translation_dataset import TranslationDataset

from .notification import Notification

__all__ = [
    "RoleEnum", "LangueEnum", "TypeExerciceEnum", "TypeInteractionEnum", "ModeConnexionEnum",
    "Utilisateur", "Apprenant", "Parent", "parent_apprenant", "Enseignant",
    "Matiere", "Lecon", "Exercice", "ContenuOffline",
    "SessionApprentissage", "ReponseExercice", "ProgressionLecon", "ProfilLinguistique", "InteractionVocale",
    "AIModel", "PromptTemplate", "Skill", "StudentSkill", "LearningPath", "LearningPathLecon", "Recommendation", "VoiceDataset", "TranslationDataset",
    "Notification"
]
