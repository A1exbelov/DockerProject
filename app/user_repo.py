from typing import Type, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from skladdb.schemas import ClientSchema
from skladdb.models import clients
from app.config import settings


class ClientRepository:
    _collection: Type[clients] = clients

    async def get_all_clients(self, session: AsyncSession) -> list[ClientSchema]:
        """Получение списка всех клиентов."""
        query = text(f"SELECT * FROM {settings.POSTGRES_SCHEMA}.clients;")
        result = await session.execute(query)
        clients = result.mappings().all()
        return [ClientSchema.model_validate(obj=client) for client in clients]

