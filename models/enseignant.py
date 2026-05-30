import uuid
from sqlalchemy import Column, String, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.database import Base

class Enseignant(Base):
    __tablename__ = "enseignants"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=func.gen_random_uuid())
    utilisateur_id = Column(UUID(as_uuid=True), ForeignKey("utilisateurs.id", ondelete="CASCADE"), unique=True, nullable=False)
    etablissement = Column(String(200), nullable=True)
    specialite = Column(String(100), nullable=True)

    # Relations
    utilisateur = relationship("Utilisateur", back_populates="enseignant")

    def __repr__(self):
        return f"<Enseignant {self.specialite} @ {self.etablissement}>"
