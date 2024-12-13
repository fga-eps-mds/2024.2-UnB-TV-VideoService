from sqlalchemy.orm import Session
from domain import fileSchema
from model import fileModel
from fastapi import HTTPException
from datetime import datetime

def create_file(file: fileSchema.FileUploadCreate, db: Session):
    # Cria um novo arquivo no banco de dados
    db_file = fileModel.FileUpload(
        filename=filename,  # Nome do arquivo
        content_type=content_type,  # Tipo MIME do arquivo
        content=content,  # Conteúdo do arquivo
        uploaded_at=datetime.utcnow(),  # Horário do upload
    )
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    return db_file

def get_file_by_id(db: Session, file_id: str):
    file_entry = db.query(fileModel.FileUpload).filter(fileModel.FileUpload.id == file_id).first()
    if not file_entry:
        raise HTTPException(status_code=404, detail="File not found")
    return file_entry

def remove_file(db: Session, file_id: str):
    file_entry = db.query(fileModel.FileUpload).filter(fileModel.FileUpload.id == file_id).first()
    if file_entry:
        db.delete(file_entry)
        db.commit()
        return {"message": "File deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="File not found")

def get_all_files(db: Session):
    # Retorna todos os arquivos armazenados no banco
    return db.query(fileModel.FileUpload).all()
