from pathlib import Path

from app.schemas.workout import WorkoutSession


class JsonStore:
    def __init__(self, root: Path):
        self.root = root

    def save_workout(
        self,
        workout: WorkoutSession,
    ) -> None:

        self.root.mkdir(
            parents=True,
            exist_ok=True,
        )

        file = self.root / f"{workout.id}.json"

        file.write_text(workout.model_dump_json(indent=2))
