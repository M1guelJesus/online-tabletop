from fastapi import WebSocket, Cookie, Query, WebSocketException, status
from typing import Annotated


class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def send_personal_message_to_first(self, message: str):
        if len(self.active_connections) == 0:
            # TODO Alter exception to an appropriate one
            raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
        await self.active_connections[0].send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

    async def broadcast_except_to_sender(self, sender: WebSocket, message: str):
        for connection in self.active_connections:
            if connection != sender:
                await connection.send_text(message)


async def get_cookie_or_token(
    session: Annotated[str | None, Cookie()] = None,
    token: Annotated[str | None, Query()] = None,
):
    if session is None and token is None:
        raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
    return session or token


wsmanager = ConnectionManager()
