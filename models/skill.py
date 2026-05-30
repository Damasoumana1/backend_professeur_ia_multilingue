import uuid
from datetime import datetime
from sqlalchemy import Column, String, Text, Integer, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.database import Base

class Skill(Base):
    __tablename__ = "skills"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=func.gen_random_uuid())
    nom = Column(String(150), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    matiere_id = Column(UUID(as_uuid=True), ForeignKey("matieres.id", ondelete="SET NULL"), nullable=True, index=True)
    niveau_difficulte = Column(Integer, default=1, nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow, server_default=func.now(), nullable=False)

    # Relations
    matiere = relationship("Matiere", back_populates="skills")
    student_skills = relationship("StudentSkill", back_populates="skill", cascade="all, delete-orphan")
    recommendations = relationship("Recommendation", back_populates="skill")

    def __repr__(self):
        return f"<Skill {self.nom} niv={self.niveau_difficulte}>"
