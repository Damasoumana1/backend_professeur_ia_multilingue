import uuid
from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.database import Base

class Apprenant(Base):
    __tablename__ = "apprenants"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=func.gen_random_uuid())
    utilisateur_id = Column(UUID(as_uuid=True), ForeignKey("utilisateurs.id", ondelete="CASCADE"), unique=True, nullable=False)
    niveau_scolaire = Column(Integer, nullable=False)
    score_global = Column(Float, default=0.0, nullable=False)
    sessions_totales = Column(Integer, default=0, nullable=False)
    derniere_activite = Column(DateTime(timezone=True), nullable=True)

    # Relations
    utilisateur = relationship("Utilisateur", back_populates="apprenant")
    parents = relationship("Parent", secondary="parent_apprenant", back_populates="apprenants")
    sessions = relationship("SessionApprentissage", back_populates="apprenant", cascade="all, delete-orphan")
    profils_linguistiques = relationship("ProfilLinguistique", back_populates="apprenant", cascade="all, delete-orphan")
    progressions = relationship("ProgressionLecon", back_populates="apprenant", cascade="all, delete-orphan")
    student_skills = relationship("StudentSkill", back_populates="apprenant", cascade="all, delete-orphan")
    learning_paths = relationship("LearningPath", back_populates="apprenant", cascade="all, delete-orphan")
    recommendations = relationship("Recommendation", back_populates="apprenant", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Apprenant niveau={self.niveau_scolaire} score={self.score_global}>"
