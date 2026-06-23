from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi import BackgroundTasks

import os
from uuid import uuid4

router = APIRouter(
    prefix="/files",
    tags=["Files"]
)

ALLOWED_EXTENSIONS = {".pdf", ".png", ".jpg", ".jpeg"}

def process_file(filename: str):
    print(f"Procesando archivo: {filename}")

# Endpoint para subir archivos
@router.post("/upload")
async def upload_file(
    background_tasks: BackgroundTasks,
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
        buffer.write(content)

    background_tasks.add_task(process_file, unique_filename)    # Añade la tarea de procesamiento al background

    return {
        "filename": unique_filename,
        "path": file_path
    }
