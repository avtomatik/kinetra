from fastapi import APIRouter

from app.schemas.workout import WorkoutSession

router = APIRouter(
    prefix="/workouts",
    tags=["workouts"],
)


@router.post(
    "",
    response_model=WorkoutSession,
)
def create_workout(
    workout: WorkoutSession,
):
    return workout


@router.get("/{workout_id}")
def get_workout(
    workout_id: str,
): ...
