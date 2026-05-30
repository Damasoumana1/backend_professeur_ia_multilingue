import uuid
from datetime import datetime
from sqlalchemy import Column, String, Float, Integer, Boolean, DateTime, Enum, func
from sqlalchemy.dialects.postgresql import UUID

from core.database import Base
from models.enums import LangueEnum

class VoiceDataset(Base):
    __tablename__ = "voice_datasets"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=func.gen_random_uuid())
    langue = Column(Enum(LangueEnum), nullable=False, index=True)
    nom = Column(String(150), nullable=False)
    source = Column(String(255), nullable=False)
    nb_audios = Column(Integer, default=0, nullable=False)
    duree_heures = Column(Float, default=0.0, nullable=False)
    version = Column(String(50), default="1.0.0", nullable=False)
    valide = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow, server_default=func.now(), nullable=False)

    def __repr__(self):
        return f"<VoiceDataset {self.nom} [{self.langue.value}]>"
