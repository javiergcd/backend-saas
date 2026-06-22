from fastapi import APIRouter, WebSocket

router = APIRouter()

@router.websocket("/ws")
async def websocker_endpoint(websocket: WebSocket):
    await websocket.accept()

    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Echo: {data}")
