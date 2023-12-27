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
            CREATE TABLE IF NOT EXISTS users(
            id BIGINT NOT NULL PRIMARY KEY, 
            phone_number VARCHAR(255) NOT NULL,
            first_name VARCHAR(255),
            last_name VARCHAR(255)
            );
            """
        )

    async def add_new_user_to_the_table(self, id, phone_number, first_name, last_name):
        sql = "INSERT INTO users(id, phone_number, first_name, last_name) " \
              "VALUES($1, $2, $3, $4);"
        try:
            await self.pool.execute(sql, id, phone_number, first_name, last_name)
        except asyncpg.exceptions.UniqueViolationError:
            pass

    async def take_a_data(self, id):
        sql = "SELECT phone_number, first_name, last_name FROM users WHERE id=$1;"
        try:
            async with self.pool.acquire() as conn:
                all = await conn.fetch(sql, id)

                answer = []
                for i in all:
                    answer.append([i[0], i[1], i[2]])
                return answer
        except asyncpg.exceptions.UniqueViolationError:
            pass


