from sqlalchemy import Column, BigInteger, String
from app.database import Base


class clients(Base):
    __tablename__ = "clients"

    id_client = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    contact_info = Column(String(255))

