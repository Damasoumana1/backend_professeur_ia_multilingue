import uuid
from datetime import datetime
from sqlalchemy import Column, Float, Integer, DateTime, ForeignKey, Enum, func, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.database import Base
from models.enums import LangueEnum

class ProfilLinguistique(Base):
    __tablename__ = "profils_linguistiques"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=func.gen_random_uuid())
    apprenant_id = Column(UUID(as_uuid=True), ForeignKey("apprenants.id", ondelete="CASCADE"), nullable=False, index=True)
    langue = Column(Enum(LangueEnum), nullable=False)
    niveau_comprehension = Column(Float, default=0.0, nullable=False)
    niveau_oral = Column(Float, default=0.0, nullable=False)
    interactions_totales = Column(Integer, default=0, nullable=False)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, server_default=func.now(), onupdate=datetime.utcnow, nullable=False)

    __table_args__ = (
        UniqueConstraint('apprenant_id', 'langue', name='uq_profils_apprenant_langue'),
    )

    # Relations
    apprenant = relationship("Apprenant", back_populates="profils_linguistiques")

    def __repr__(self):
        return f"<ProfilLinguistique {self.langue.value} comp={self.niveau_comprehension}>"
