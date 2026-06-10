from pydantic import BaseModel


class Exercise(BaseModel):
    id: str

    name: str

    aliases: list[str] = []

    category: str

    equipment: list[str] = []

    primary_muscles: list[str] = []
