import json
import uuid
from datetime import datetime
from pathlib import Path

from app.exercise_catalog.catalog import ExerciseCatalog
from app.schemas.workout import ExerciseBlock, SetEntry, WorkoutSession

catalog = ExerciseCatalog()


def convert_set(
    raw_set: dict,
) -> dict:

    metrics = {}

    if "weight" in raw_set:
        metrics["weight_kg"] = raw_set["weight"]

    if "reps" in raw_set:
        metrics["reps"] = raw_set["reps"]

    if "duration_sec" in raw_set:
        metrics["duration_sec"] = raw_set["duration_sec"]

    if "rest" in raw_set:
        metrics["rest_min"] = raw_set["rest"]

    if "reps_per_side" in raw_set:
        metrics["reps_per_side"] = raw_set["reps_per_side"]

    #
    # Preserve any future legacy fields
    # we didn't explicitly map.
    #
    known = {
        "weight",
        "reps",
        "duration_sec",
        "rest",
        "reps_per_side",
    }

    for key, value in raw_set.items():
        if key not in known:
            metrics[key] = value

    return metrics


def resolve_exercise_id(
    exercise_name: str,
) -> str:
    """
    Convert legacy names to canonical ids.

    Unknown exercises become a stable slug.
    """

    exercise = catalog.find_by_alias(exercise_name)

    if exercise:
        return exercise.id

    return (
        exercise_name.lower()
        .replace("/", "_")
        .replace("-", "_")
        .replace(" ", "_")
    )


def load_legacy_workout(
    path: Path,
) -> list[WorkoutSession]:

    raw_data = json.loads(path.read_text())

    workouts: list[WorkoutSession] = []

    for date_str, exercises in raw_data.items():

        exercise_blocks = []

        for exercise_order, (
            exercise_name,
            raw_sets,
        ) in enumerate(
            exercises.items(),
            start=1,
        ):

            sets = []

            for set_order, raw_set in enumerate(
                raw_sets,
                start=1,
            ):

                sets.append(
                    SetEntry(
                        order=set_order,
                        metrics=convert_set(raw_set),
                        notes=raw_set.get("notes"),
                    )
                )

            exercise_blocks.append(
                ExerciseBlock(
                    exercise_id=resolve_exercise_id(exercise_name),
                    order=exercise_order,
                    sets=sets,
                )
            )

        #
        # Legacy format only stores date.
        #
        # Use midnight local time.
        #
        started_at = datetime.fromisoformat(date_str)

        workouts.append(
            WorkoutSession(
                id=uuid.uuid4(),
                user_id=uuid.uuid4(),
                started_at=started_at,
                exercises=exercise_blocks,
            )
        )

    return workouts
