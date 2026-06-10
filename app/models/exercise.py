import uuid

from sqlalchemy import ForeignKey, Integer, Text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class ExerciseBlockModel(Base):
    __tablename__ = "exercise_blocks"

    id = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
    )

    workout_id = mapped_column(ForeignKey("workout_sessions.id"))

    exercise_id = mapped_column()

    order = mapped_column(Integer)


class SetEntryModel(Base):
    __tablename__ = "set_entries"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
    )

    exercise_block_id = mapped_column(ForeignKey("exercise_blocks.id"))

    order = mapped_column(Integer)

    metrics = mapped_column(JSONB)

    notes = mapped_column(
        Text,
        nullable=True,
    )
