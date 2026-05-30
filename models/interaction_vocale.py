import uuid
from datetime import datetime
from sqlalchemy import Column, String, Text, Float, Integer, DateTime, ForeignKey, Enum, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.database import Base
from models.enums import TypeInteractionEnum, LangueEnum

class InteractionVocale(Base):
    __tablename__ = "interactions_vocales"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=func.gen_random_uuid())
    session_id = Column(UUID(as_uuid=True), ForeignKey("sessions_apprentissage.id", ondelete="CASCADE"), nullable=False, index=True)
    type_interaction = Column(Enum(TypeInteractionEnum), nullable=False)
    langue_detectee = Column(Enum(LangueEnum), nullable=False, index=True)
    score_confiance_stt = Column(Float, nullable=True)
    texte_transcrit = Column(Text, nullable=True)
    reponse_llm = Column(Text, nullable=True)
    chemin_audio_input = Column(String(500), nullable=True)
    chemin_audio_output = Column(String(500), nullable=True)
    duree_traitement_ms = Column(Integer, default=0, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow, server_default=func.now(), nullable=False, index=True)

    # Relations
    session = relationship("SessionApprentissage", back_populates="interactions_vocales")

    def __repr__(self):
        return f"<InteractionVocale [{self.type_interaction.value}] conf={self.score_confiance_stt}>"
