from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from skladdb.schemas import ClientSchema
from skladdb.models import clients
from app.database import database
from app.user_repo import ClientRepository

client_router = APIRouter()
client_repo = ClientRepository()


@client_router.get(
    "/clients",
    response_model=list[ClientSchema],
    status_code=status.HTTP_200_OK,
)
async def get_all_client() -> list[ClientSchema]:
    """Получение всех клиентов."""
    async with database.session() as session:
        clients = await client_repo.get_all_clients(session=session)

    return clients


