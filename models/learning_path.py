import uuid
from datetime import datetime
from sqlalchemy import Column, String, Text, Boolean, Integer, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.database import Base

class LearningPathLecon(Base):
    __tablename__ = "learning_path_lecons"

    path_id = Column(UUID(as_uuid=True), ForeignKey("learning_paths.id", ondelete="CASCADE"), primary_key=True)
    lecon_id = Column(UUID(as_uuid=True), ForeignKey("lecons.id", ondelete="CASCADE"), primary_key=True)
    ordre = Column(Integer, default=1, nullable=False)
    completee = Column(Boolean, default=False, nullable=False)

    # Relations
    path = relationship("LearningPath", back_populates="lecons_assoc")
    lecon = relationship("Lecon", back_populates="learning_path_lecons")


class LearningPath(Base):
    __tablename__ = "learning_paths"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=func.gen_random_uuid())
    apprenant_id = Column(UUID(as_uuid=True), ForeignKey("apprenants.id", ondelete="CASCADE"), nullable=False, index=True)
    nom = Column(String(150), nullable=True)
    description = Column(Text, nullable=True)
    actif = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, server_default=func.now(), onupdate=datetime.utcnow, nullable=False)

    # Relations
    apprenant = relationship("Apprenant", back_populates="learning_paths")
    lecons_assoc = relationship("LearningPathLecon", back_populates="path", cascade="all, delete-orphan", order_by="LearningPathLecon.ordre")
    recommendations = relationship("Recommendation", back_populates="path")

    def __repr__(self):
        return f"<LearningPath {self.nom} actif={self.actif}>"
