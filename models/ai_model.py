import uuid
from datetime import datetime
from sqlalchemy import Column, String, Float, Boolean, DateTime, func, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.database import Base

class AIModel(Base):
    __tablename__ = "ai_models"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=func.gen_random_uuid())
    nom = Column(String(100), nullable=False)
    version = Column(String(50), nullable=False)
    fournisseur = Column(String(100), nullable=False)
    type_modele = Column(String(50), nullable=False, index=True)
    precision = Column(Float, default=0.0, nullable=False)
    actif = Column(Boolean, default=True, nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow, server_default=func.now(), nullable=False)

    __table_args__ = (
        UniqueConstraint('nom', 'version', name='uq_ai_models_nom_version'),
    )

    # Relations
    prompts = relationship("PromptTemplate", back_populates="modele", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<AIModel {self.nom} v{self.version} ({self.type_modele})>"
