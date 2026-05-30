import uuid
from sqlalchemy import Column, String, Boolean, ForeignKey, Table, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.database import Base

parent_apprenant = Table(
    "parent_apprenant",
    Base.metadata,
    Column("parent_id", UUID(as_uuid=True), ForeignKey("parents.id", ondelete="CASCADE"), primary_key=True),
    Column("apprenant_id", UUID(as_uuid=True), ForeignKey("apprenants.id", ondelete="CASCADE"), primary_key=True),
)

class Parent(Base):
    __tablename__ = "parents"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=func.gen_random_uuid())
    utilisateur_id = Column(UUID(as_uuid=True), ForeignKey("utilisateurs.id", ondelete="CASCADE"), unique=True, nullable=False)
    telephone = Column(String(20), nullable=True)
    notifications_actives = Column(Boolean, default=True, nullable=False)

    # Relations
    utilisateur = relationship("Utilisateur", back_populates="parent")
    apprenants = relationship("Apprenant", secondary=parent_apprenant, back_populates="parents")

    def __repr__(self):
        return f"<Parent tel={self.telephone}>"
