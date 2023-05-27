import asyncio
import asyncpg

from data import config


class DataBase:
    def __init__(self):
        loop = asyncio.get_event_loop()
        self.pool: asyncio.pool.Pool = loop.run_until_complete(
            asyncpg.create_pool(
                user=config.PGUSER,
                database=config.DBNAME,
                password=config.PGPASSWORD,
                host=config.IP,
                port=config.DBPORT,
                loop=loop
            )
        )

    async def create_table_users(self):
        await self.pool.execute(
            """
            CREATE TABLE IF NOT EXISTS users_of_SB 
            (
            id BIGINT NOT NULL PRIMARY KEY, 
            phone_number VARCHAR(255) NOT NULL
            );
            """
        )

