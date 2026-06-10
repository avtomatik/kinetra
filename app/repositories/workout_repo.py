from sqlalchemy.orm import Session

from app.models.workout import WorkoutSessionModel


class WorkoutRepository:

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def save(
        self,
        workout,
    ):
        """
        TODO:
        Persist ExerciseBlockModel
        Persist SetEntryModel

        Current implementation only stores
        WorkoutSession metadata.
        """

        model = WorkoutSessionModel(
            id=workout.id,
            user_id=workout.user_id,
            started_at=workout.started_at,
            ended_at=workout.ended_at,
            notes=workout.notes,
        )

        self.db.add(model)

        self.db.commit()

        return model

    def get(
        self,
        workout_id,
    ):

        return (
            self.db.query(WorkoutSessionModel)
            .filter(WorkoutSessionModel.id == workout_id)
            .first()
        )
