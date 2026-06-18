from fastapi import APIRouter, UploadFile, File, HTTPException

import os
from uuid import uuid4

router = APIRouter(
    prefix="/files",
    tags=["Files"]
)

ALLOWED_EXTENSIONS = [".pdf", ".png", ".jpg", ".jpeg"]

# Endpoint para subir archivos
@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...)
):
    extension = os.path.splitext(file.filename)[1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400, 
            detail="Tipo de archivo no permitido"
        )
    
    content = await file.read()
    MAX_FILE_SIZE = 5 * 1024 * 1024 # 5MB
    
    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400, 
            detail="Archivo demasiado grande"
        )

    unique_filename = (f"{uuid4()}-{file.filename}")

    file_path = os.path.join("uploads", unique_filename)

    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)

    return {
        "filename": unique_filename,
        "path": file_path
    }
