import uuid
from datetime import datetime
from sqlalchemy import Column, String, Text, Boolean, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.database import Base

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=func.gen_random_uuid())
    destinataire_id = Column(UUID(as_uuid=True), ForeignKey("utilisateurs.id", ondelete="CASCADE"), nullable=False, index=True)
    type_notif = Column(String(50), nullable=False)
    titre = Column(String(200), nullable=False)
    message = Column(Text, nullable=False)
    lue = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow, server_default=func.now(), nullable=False)
    lue_le = Column(DateTime(timezone=True), nullable=True)

    # Relations
    destinataire = relationship("Utilisateur", back_populates="notifications")

    def __repr__(self):
        return f"<Notification '{self.titre}' lue={self.lue}>"
