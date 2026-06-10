from app.repositories.workout_repo import WorkoutRepository
from app.schemas.workout import WorkoutSession


class WorkoutService:
    def __init__(
        self,
        repository: WorkoutRepository,
    ):
        self.repository = repository

    def create_workout(
        self,
        workout: WorkoutSession,
    ) -> WorkoutSession:
        self.repository.save(workout)
        return workout

    def get_workout(
        self,
        workout_id,
    ):
        return self.repository.get(workout_id)
