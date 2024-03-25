from fastapi import WebSocket, APIRouter, Depends
from src.api.dependencies.auth import Auth
from src.utils.redis import redis

import aioredis
import asyncio
import async_timeout


router = APIRouter()
STOPWORD = "STOP"

# todo check that redis pool is created once
# todo share pool between workers
@router.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket, auth: Auth = Depends()):
    await websocket.accept()
    # try:
    #     user = await auth.check_access_token_websocket(websocket)
    # except Exception as e:
    #     await websocket.send_text('Unauthenticated')
    #     await websocket.close()
    #     return

    redis_connection = redis.get_connection()
    psub = redis_connection.pubsub()

    async def reader(channel: aioredis.client.PubSub, websocket):
        while True:
            try:
                message = await channel.get_message(ignore_subscribe_messages=True)
                if message is not None:
                    await websocket.send_text(type(message))
                await asyncio.sleep(1)
            except asyncio.TimeoutError:
                pass

    async with psub as p:
        await p.subscribe("channel:1")
        await reader(p, websocket)  # wait for reader to complete
        await p.unsubscribe("channel:1")
    await psub.close()
    await websocket.close()


@router.websocket("/ws/chat/huy")
async def websocket_endpoint(websocket: WebSocket, auth: Auth = Depends()):
    await websocket.accept()
    await websocket.send_text('type smth')
    msg = await websocket.receive_text()

    channel_name = 'channel:1'
    pub = redis.get_connection()
    await pub.publish(channel_name, msg)
    await pub.close()
    await websocket.close()
