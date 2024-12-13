from pydantic import BaseModel

class FileUploadBase(BaseModel):
    filename: str  # Nome do arquivo
    content_type: str 
    content: bytes  # Conteúdo do arquivo de transcrição


class FileUploadCreate(FileUploadBase):
    pass

class FileUploadResponse(FileUploadBase):
    id: str        # ID do arquivo (UUID)
    uploaded_at: str  # Data de upload

    class Config:
        orm_mode = True  # Permite que os modelos possam ser convertidos de/para modelos ORM
