import uuid
from datetime import datetime
from sqlalchemy import Column, Float, Integer, DateTime, ForeignKey, func, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.database import Base

class StudentSkill(Base):
    __tablename__ = "student_skills"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=func.gen_random_uuid())
    apprenant_id = Column(UUID(as_uuid=True), ForeignKey("apprenants.id", ondelete="CASCADE"), nullable=False, index=True)
    skill_id = Column(UUID(as_uuid=True), ForeignKey("skills.id", ondelete="CASCADE"), nullable=False)
    score_maitrise = Column(Float, default=0.0, nullable=False, index=True)
    derniere_evaluation = Column(DateTime(timezone=True), nullable=True)
    nb_evaluations = Column(Integer, default=0, nullable=False)

    __table_args__ = (
        UniqueConstraint('apprenant_id', 'skill_id', name='uq_student_skills_apprenant_skill'),
    )

    # Relations
    apprenant = relationship("Apprenant", back_populates="student_skills")
    skill = relationship("Skill", back_populates="student_skills")

    def __repr__(self):
        return f"<StudentSkill maitrise={self.score_maitrise}>"
