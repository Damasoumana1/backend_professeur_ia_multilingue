import uuid
from datetime import datetime
from sqlalchemy import Column, String, Text, Boolean, DateTime, ForeignKey, Enum, func, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.database import Base
from models.enums import LangueEnum

class PromptTemplate(Base):
    __tablename__ = "prompt_templates"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=func.gen_random_uuid())
    modele_id = Column(UUID(as_uuid=True), ForeignKey("ai_models.id", ondelete="CASCADE"), nullable=False, index=True)
    nom = Column(String(100), nullable=False)
    langue = Column(Enum(LangueEnum), nullable=False, index=True)
    template = Column(Text, nullable=False)
    description = Column(Text, nullable=True)
    actif = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, server_default=func.now(), onupdate=datetime.utcnow, nullable=False)

    __table_args__ = (
        UniqueConstraint('nom', 'langue', name='uq_prompt_templates_nom_langue'),
    )

    # Relations
    modele = relationship("AIModel", back_populates="prompts")

    def __repr__(self):
        return f"<PromptTemplate {self.nom} [{self.langue.value}]>"
