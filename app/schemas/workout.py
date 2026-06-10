from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from .common import Metrics


class SetEntry(BaseModel):
    order: int
    metrics: Metrics
    notes: str | None = None


class ExerciseBlock(BaseModel):
    exercise_id: str
    order: int
    sets: list[SetEntry]
    notes: str | None = None


class WorkoutSession(BaseModel):
    id: UUID

    user_id: UUID

    started_at: datetime
    ended_at: datetime | None = None

    exercises: list[ExerciseBlock]

    notes: str | None = None
