import enum

class RoleEnum(str, enum.Enum):
    APPRENANT  = "apprenant"
    PARENT     = "parent"
    ENSEIGNANT = "enseignant"
    ADMIN      = "admin"

class LangueEnum(str, enum.Enum):
    FRANCAIS = "fr"
    MOORE    = "moore"
    DIOULA   = "dioula"

class TypeExerciceEnum(str, enum.Enum):
    QCM           = "qcm"
    VRAI_FAUX     = "vrai_faux"
    TEXTE_LIBRE   = "texte_libre"
    ASSOCIATION   = "association"
    ORAL          = "oral"

class TypeInteractionEnum(str, enum.Enum):
    QUESTION      = "question"
    REFORMULATION = "reformulation"
    AIDE          = "aide"
    CORRECTION    = "correction"

class ModeConnexionEnum(str, enum.Enum):
    EN_LIGNE     = "online"
    HORS_LIGNE   = "offline"
