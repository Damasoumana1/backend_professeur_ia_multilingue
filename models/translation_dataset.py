import uuid
from datetime import datetime
from sqlalchemy import Column, String, Integer, Boolean, DateTime, Enum, func
from sqlalchemy.dialects.postgresql import UUID

from core.database import Base
from models.enums import LangueEnum

class TranslationDataset(Base):
    __tablename__ = "translation_datasets"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=func.gen_random_uuid())
    langue_source = Column(Enum(LangueEnum), nullable=False)
    langue_cible = Column(Enum(LangueEnum), nullable=False)
    nom = Column(String(150), nullable=False)
    source = Column(String(255), nullable=False)
    nb_paires = Column(Integer, default=0, nullable=False)
    version = Column(String(50), default="1.0.0", nullable=False)
    valide = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow, server_default=func.now(), nullable=False)

    def __repr__(self):
        return f"<TranslationDataset {self.langue_source.value}->{self.langue_cible.value}>"
