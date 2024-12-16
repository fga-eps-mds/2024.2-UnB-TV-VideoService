from pydantic import BaseModel

class FileBase(BaseModel):
    filename: str  # Nome do arquivo
    content_type: str 
    content: bytes  # Conteúdo do arquivo de transcrição


class FileCreate(FileBase):
    pass

class FileResponse(FileBase):
    id: str        # ID do arquivo (UUID)
    uploaded_at: str  # Data de upload

    class Config:
        orm_mode = True  # Permite que os modelos possam ser convertidos de/para modelos ORM
