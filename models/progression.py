import uuid
from sqlalchemy import Column, Float, Integer, Boolean, DateTime, ForeignKey, func, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.database import Base

class ProgressionLecon(Base):
    __tablename__ = "progressions_lecons"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=func.gen_random_uuid())
    apprenant_id = Column(UUID(as_uuid=True), ForeignKey("apprenants.id", ondelete="CASCADE"), nullable=False, index=True)
    lecon_id = Column(UUID(as_uuid=True), ForeignKey("lecons.id", ondelete="CASCADE"), nullable=False, index=True)
    pourcentage_complete = Column(Float, default=0.0, nullable=False)
    tentatives = Column(Integer, default=0, nullable=False)
    meilleur_score = Column(Float, default=0.0, nullable=False)
    completee = Column(Boolean, default=False, nullable=False)
    derniere_tentative = Column(DateTime(timezone=True), nullable=True)

    __table_args__ = (
        UniqueConstraint('apprenant_id', 'lecon_id', name='uq_progression_apprenant_lecon'),
    )

    # Relations
    apprenant = relationship("Apprenant", back_populates="progressions")
    lecon = relationship("Lecon", back_populates="progressions")

    def __repr__(self):
        return f"<Progression {self.pourcentage_complete}% completee={self.completee}>"
