import redis.asyncio as redis
from .settings import settings

redis_client = redis.from_url(
    f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}",
    db=0,
    decode_responses=True
)
