from app.core.redis import redis_client

PREFIX = "email_verify"
TTL = 600


def _create_key(email: str) -> str:
    return f"{PREFIX}:{email}"


async def save_code(email: str, code: str) -> None:
    await redis_client.setex(_create_key(email), TTL, code)


async def get_code(email: str) -> str | None:
    return await redis_client.get(_create_key(email))


async def delete_code(email: str) -> None:
    await redis_client.delete(_create_key(email))
