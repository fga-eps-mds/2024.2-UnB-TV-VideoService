from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from domain import fileSchema
from database import get_db
from repository import fileRepository
from starlette.responses import JSONResponse

FileUpload = APIRouter(
    prefix="/file-upload"
)

@FileUpload.post("/")
def upload_file(file: fileSchema.FileUploadCreate, db: Session = Depends(get_db)):
    # Endpoint para fazer upload de um arquivo.
    try:
        # Chama a função do repositório para criar o arquivo no banco de dados
        db_file = fileRepository.create_file(db=db, file=file)
        return JSONResponse(status_code=201, content={"id": db_file.id, "filename": db_file.filename, "uploaded_at": db_file.uploaded_at})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@FileUpload.get("/{file_id}")
def get_file(file_id: str, db: Session = Depends(get_db)):
    # Endpoint para obter um arquivo pelo ID
    try:
        # Chama a função do repositório para obter o arquivo do banco de dados
        db_file = fileRepository.get_file_by_id(db=db, file_id=file_id)
        return {"id": db_file.id, "filename": db_file.filename, "uploaded_at": db_file.uploaded_at}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@FileUpload.delete("/{file_id}")
def delete_file(file_id: str, db: Session = Depends(get_db)):
    # Endpoint para deletar um arquivo pelo ID
    try:
        # Chama a função do repositório para remover o arquivo
        response = fileRepository.remove_file(db=db, file_id=file_id)
        return response
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@FileUpload.get("/")
def get_all_files(db: Session = Depends(get_db)):
    # Endpoint para obter todos os arquivos
    try:
        # Chama a função do repositório para obter todos os arquivos
        files = fileRepository.get_all_files(db=db)
        return {"files": files}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
