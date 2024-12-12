from sqlalchemy.orm import Session
from domain import fileSchema
from model import fileModel
from fastapi import HTTPException

def create_file(db: Session, file: fileSchema.FileUploadCreate):
    # Cria um novo arquivo no banco de dados
    db_file = fileModel.FileUpload(
        filename=file.filename.strip(),
        content=file.content.strip(),
        uploaded_at= datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")  # Aqui você pode usar o datetime para salvar a data atual
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
