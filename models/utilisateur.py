import uuid
from datetime import datetime
from sqlalchemy import Column, String, Boolean, DateTime, Enum, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.database import Base
from models.enums import RoleEnum, LangueEnum

class Utilisateur(Base):
    __tablename__ = "utilisateurs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=func.gen_random_uuid())
    nom = Column(String(100), nullable=False)
    prenom = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    mot_de_passe = Column(String(255), nullable=False)
    date_naissance = Column(DateTime, nullable=True)
    role = Column(Enum(RoleEnum), nullable=False, index=True)
    langue_preferee = Column(Enum(LangueEnum), default=LangueEnum.FRANCAIS, server_default=LangueEnum.FRANCAIS.value, nullable=False)
    est_actif = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, server_default=func.now(), onupdate=datetime.utcnow, nullable=False)

    # Relations
    apprenant = relationship("Apprenant", back_populates="utilisateur", uselist=False, cascade="all, delete-orphan")
    parent = relationship("Parent", back_populates="utilisateur", uselist=False, cascade="all, delete-orphan")
    enseignant = relationship("Enseignant", back_populates="utilisateur", uselist=False, cascade="all, delete-orphan")
    notifications = relationship("Notification", back_populates="destinataire", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Utilisateur {self.prenom} {self.nom} [{self.role.value}]>"
