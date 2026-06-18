from fastapi import APIRouter, UploadFile, File

router = APIRouter(
    prefix="/files",
    tags=["Files"]
)

# Endpoint para subir archivos
@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...)
):
    return {
        "filename": file.filename,
        "content_type": file.content_type
    }
