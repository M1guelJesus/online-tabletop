from fastapi import APIRouter, WebSocket, Depends, WebSocketDisconnect
from typing import Annotated
from ws import get_cookie_or_token, wsmanager
import json

ws_router = APIRouter(
    prefix="/ws",
    tags=["WebSockets"],
)


@ws_router.websocket("")
async def ws(
    websocket: WebSocket,
    cookie_or_token: Annotated[str, Depends(get_cookie_or_token)],
):
    await wsmanager.connect(websocket=websocket)
    try:
        while True:
            data = await websocket.receive_text()
            json_data = json.loads(data)
            if json_data["socketType"] == "loadExisting":
                await wsmanager.send_personal_message_to_first(message=data)
            else:
                await wsmanager.broadcast(message=data)
    except WebSocketDisconnect:
        wsmanager.disconnect(websocket=websocket)
