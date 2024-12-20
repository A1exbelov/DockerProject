from pydantic import BaseModel, ConfigDict


class ClientSchema(BaseModel):
    id_client: int
    name: str
    contact_info: str

    model_config = ConfigDict(from_attributes=True)