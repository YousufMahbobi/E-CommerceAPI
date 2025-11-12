import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from app.core.config import settings

async def test_connection():
    try:
        # Make sure your DATABASE_URL includes +asyncpg
        engine = create_async_engine(settings.DATABASE_URL, echo=True)
        async with engine.begin() as conn:
            await conn.run_sync(lambda _: print("Connected to DB!"))
        await engine.dispose()
    except Exception as e:
        print("Connection failed:", e)

if __name__ == "__main__":
    asyncio.run(test_connection())
