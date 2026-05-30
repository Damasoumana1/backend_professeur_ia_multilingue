import uuid
from datetime import datetime
from sqlalchemy import Column, Float, Integer, DateTime, ForeignKey, Enum, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.database import Base
from models.enums import LangueEnum, ModeConnexionEnum

class SessionApprentissage(Base):
    __tablename__ = "sessions_apprentissage"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=func.gen_random_uuid())
    apprenant_id = Column(UUID(as_uuid=True), ForeignKey("apprenants.id", ondelete="CASCADE"), nullable=False, index=True)
    lecon_id = Column(UUID(as_uuid=True), ForeignKey("lecons.id", ondelete="RESTRICT"), nullable=False, index=True)
    debut = Column(DateTime(timezone=True), default=datetime.utcnow, server_default=func.now(), nullable=False, index=True)
    fin = Column(DateTime(timezone=True), nullable=True)
    duree_secondes = Column(Integer, default=0, nullable=False)
    langue_utilisee = Column(Enum(LangueEnum), nullable=False)
    score_session = Column(Float, default=0.0, nullable=False)
    mode_connexion = Column(Enum(ModeConnexionEnum), default=ModeConnexionEnum.EN_LIGNE, nullable=False)

    # Relations
    apprenant = relationship("Apprenant", back_populates="sessions")
    lecon = relationship("Lecon", back_populates="sessions")
    reponses_exercices = relationship("ReponseExercice", back_populates="session", cascade="all, delete-orphan")
    interactions_vocales = relationship("InteractionVocale", back_populates="session", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Session apprenant={self.apprenant_id} score={self.score_session}>"
