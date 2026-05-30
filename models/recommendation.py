import uuid
from datetime import datetime
from sqlalchemy import Column, String, Text, Float, Boolean, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.database import Base

class Recommendation(Base):
    __tablename__ = "recommendations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=func.gen_random_uuid())
    apprenant_id = Column(UUID(as_uuid=True), ForeignKey("apprenants.id", ondelete="CASCADE"), nullable=False, index=True)
    lecon_id = Column(UUID(as_uuid=True), ForeignKey("lecons.id", ondelete="SET NULL"), nullable=True)
    skill_id = Column(UUID(as_uuid=True), ForeignKey("skills.id", ondelete="SET NULL"), nullable=True)
    path_id = Column(UUID(as_uuid=True), ForeignKey("learning_paths.id", ondelete="SET NULL"), nullable=True)
    type_reco = Column(String(50), nullable=False)
    raison = Column(Text, nullable=True)
    score_confiance = Column(Float, default=0.0, nullable=False, index=True)
    appliquee = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow, server_default=func.now(), nullable=False)
    appliquee_le = Column(DateTime(timezone=True), nullable=True)

    # Relations
    apprenant = relationship("Apprenant", back_populates="recommendations")
    lecon = relationship("Lecon", back_populates="recommendations")
    skill = relationship("Skill", back_populates="recommendations")
    path = relationship("LearningPath", back_populates="recommendations")

    def __repr__(self):
        return f"<Recommendation type={self.type_reco} conf={self.score_confiance}>"
