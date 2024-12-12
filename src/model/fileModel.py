import uuid
from sqlalchemy import Column, Integer, String, Text
from database import Base  # Assumindo que sua conexão ao banco é configurada em 'database.py'

class FileUpload(Base):
    __tablename__ = "file_uploads"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))  # UUID como ID
    filename = Column(String, nullable=False)
    content = Column(Text, nullable=False) # Para armazenar o conteúdo do arquivo .txt
    uploaded_at = Column(String, nullable=False)  # Usar DateTime (?)
