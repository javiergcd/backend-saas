from fastapi import APIRouter, UploadFile, File

import os
from uuid import uuid4

router = APIRouter(
    prefix="/files",
    tags=["Files"]
)

# Endpoint para subir archivos
@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...)
):
    unique_filename = (f"{uuid4()}-{file.filename}")

    file_path = os.path.join("uploads", unique_filename)

    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)

    return {
        "filename": unique_filename,
        "path": file_path
    }
