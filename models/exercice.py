import uuid
from sqlalchemy import Column, String, Text, Integer, ForeignKey, Enum, func
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship

from core.database import Base
from models.enums import TypeExerciceEnum

class Exercice(Base):
    __tablename__ = "exercices"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=func.gen_random_uuid())
    lecon_id = Column(UUID(as_uuid=True), ForeignKey("lecons.id", ondelete="CASCADE"), nullable=False, index=True)
    type_exercice = Column(Enum(TypeExerciceEnum), nullable=False)
    enonce_fr = Column(Text, nullable=False)
    enonce_moore = Column(Text, nullable=True)
    enonce_dioula = Column(Text, nullable=True)
    options = Column(JSONB, nullable=True)
    reponse_correcte = Column(Text, nullable=False)
    niveau_difficulte = Column(Integer, default=1, nullable=False, index=True)
    points = Column(Integer, default=10, nullable=False)

    # Relations
    lecon = relationship("Lecon", back_populates="exercices")
    reponses = relationship("ReponseExercice", back_populates="exercice", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Exercice [{self.type_exercice.value}] niv={self.niveau_difficulte}>"
