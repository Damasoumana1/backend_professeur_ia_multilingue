import uuid
from sqlalchemy import Column, String, Text, Boolean, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.database import Base

class Matiere(Base):
    __tablename__ = "matieres"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=func.gen_random_uuid())
    nom = Column(String(100), nullable=False)
    code = Column(String(20), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    icone = Column(String(50), nullable=True)
    actif = Column(Boolean, default=True, nullable=False)

    # Relations
    lecons = relationship("Lecon", back_populates="matiere", order_by="Lecon.ordre", cascade="all, delete-orphan")
    skills = relationship("Skill", back_populates="matiere")

    def __repr__(self):
        return f"<Matiere {self.code}>"
