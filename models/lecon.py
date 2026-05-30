import uuid
from datetime import datetime
from sqlalchemy import Column, String, Text, Boolean, Integer, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.database import Base

class Lecon(Base):
    __tablename__ = "lecons"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=func.gen_random_uuid())
    matiere_id = Column(UUID(as_uuid=True), ForeignKey("matieres.id", ondelete="RESTRICT"), nullable=False, index=True)
    titre = Column(String(200), nullable=False)
    contenu_fr = Column(Text, nullable=False)
    contenu_moore = Column(Text, nullable=True)
    contenu_dioula = Column(Text, nullable=True)
    niveau = Column(Integer, nullable=False)
    ordre = Column(Integer, default=1, nullable=False)
    disponible_offline = Column(Boolean, default=False, nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow, server_default=func.now(), nullable=False)

    # Relations
    matiere = relationship("Matiere", back_populates="lecons")
    exercices = relationship("Exercice", back_populates="lecon", cascade="all, delete-orphan")
    contenu_offline = relationship("ContenuOffline", back_populates="lecon", uselist=False, cascade="all, delete-orphan")
    sessions = relationship("SessionApprentissage", back_populates="lecon")
    progressions = relationship("ProgressionLecon", back_populates="lecon", cascade="all, delete-orphan")
    learning_path_lecons = relationship("LearningPathLecon", back_populates="lecon", cascade="all, delete-orphan")
    recommendations = relationship("Recommendation", back_populates="lecon", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Lecon '{self.titre}' niv={self.niveau}>"
