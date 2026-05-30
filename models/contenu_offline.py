import uuid
from datetime import datetime
from sqlalchemy import Column, String, Float, Boolean, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.database import Base

class ContenuOffline(Base):
    __tablename__ = "contenus_offline"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=func.gen_random_uuid())
    lecon_id = Column(UUID(as_uuid=True), ForeignKey("lecons.id", ondelete="CASCADE"), unique=True, nullable=False)
    version = Column(String(20), default="1.0.0", nullable=False)
    taille_mo = Column(Float, nullable=True)
    chemin_fichier = Column(String(500), nullable=False)
    telecharge_le = Column(DateTime(timezone=True), nullable=True)
    est_valide = Column(Boolean, default=True, nullable=False)

    # Relations
    lecon = relationship("Lecon", back_populates="contenu_offline")

    def __repr__(self):
        return f"<ContenuOffline lecon={self.lecon_id} v={self.version}>"
