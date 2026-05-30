import uuid
from datetime import datetime
from sqlalchemy import Column, String, Text, Float, Integer, Boolean, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.database import Base

class ReponseExercice(Base):
    __tablename__ = "reponses_exercices"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=func.gen_random_uuid())
    session_id = Column(UUID(as_uuid=True), ForeignKey("sessions_apprentissage.id", ondelete="CASCADE"), nullable=False, index=True)
    exercice_id = Column(UUID(as_uuid=True), ForeignKey("exercices.id", ondelete="CASCADE"), nullable=False, index=True)
    reponse_apprenant = Column(Text, nullable=False)
    est_correcte = Column(Boolean, nullable=False)
    temps_reponse_ms = Column(Integer, default=0, nullable=False)
    tentatives = Column(Integer, default=1, nullable=False)
    score_obtenu = Column(Float, default=0.0, nullable=False)
    soumis_le = Column(DateTime(timezone=True), default=datetime.utcnow, server_default=func.now(), nullable=False)

    # Relations
    session = relationship("SessionApprentissage", back_populates="reponses_exercices")
    exercice = relationship("Exercice", back_populates="reponses")

    def __repr__(self):
        return f"<Reponse correct={self.est_correcte} score={self.score_obtenu}>"
