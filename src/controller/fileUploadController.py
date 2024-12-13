from typing import Optional
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from domain import fileSchema
from database import get_db
from repository import fileRepository
from starlette.responses import JSONResponse, StreamingResponse
from io import BytesIO
from datetime import datetime

FileUpload = APIRouter(
    prefix="/file-upload"
)

@FileUpload.post("/")
async def upload_file(
    file: UploadFile = File(...), 
    db: Session = Depends(get_db)
    ):
    # Endpoint para fazer upload de um arquivo.

    try:
        content = await file.read()
        with open(file.filename, 'wb') as f:
            f.write(content)
        # Chama a função do repositório para criar o arquivo no banco de dados
        db_file = fileRepository.create_file(
            db=db, 
            filename=file.filename, 
            content_type=file.content_type,
            content=content,
            )
        return JSONResponse(status_code=201, content={
            "fileResponse": db_file.content_type,
            "id": db_file.id, 
            "filename": db_file.filename, 
            "uploaded_at": db_file.uploaded_at
        })
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao salvar o arquivo: {str(e)}")
    finally:
        file.file.close()


@FileUpload.get("/{file_id}")
def get_file(file_id: str, db: Session = Depends(get_db)):
    # Endpoint para obter um arquivo pelo ID
    try:
        # Chama a função do repositório para obter o arquivo do banco de dados
        db_file = fileRepository.get_file_by_id(db=db, file_id=file_id)
        
        # Retorna o conteúdo do arquivo como uma resposta binária
        return StreamingResponse(BytesIO(db_file.content), media_type="application/octet-stream", headers={
            "Content-Disposition": f"attachment; filename={db_file.filename}"
        })
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao recuperar o arquivo: {str(e)}")

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
        raise HTTPException(status_code=400, detail=f"Erro ao deletar o arquivo: {str(e)}")

@FileUpload.get("/")
def get_all_files(db: Session = Depends(get_db)):
    # Endpoint para obter todos os arquivos
    try:
        # Chama a função do repositório para obter todos os arquivos
        files = fileRepository.get_all_files(db=db)
        return {"files": files}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao listar arquivos: {str(e)}")
