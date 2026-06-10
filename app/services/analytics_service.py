from app.schemas.workout import WorkoutSession


def flatten_workout(
    workout: WorkoutSession,
):
    rows = []

    for block in workout.exercises:

        for set_ in block.sets:

            row = {
                "session_id": str(workout.id),
                "exercise_id": block.exercise_id,
                "set_order": set_.order,
            }

            row.update(set_.metrics)

            rows.append(row)

    return rows
