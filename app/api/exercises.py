from fastapi import APIRouter, HTTPException

from app.exercise_catalog.catalog import ExerciseCatalog

router = APIRouter(
    prefix="/exercises",
    tags=["exercises"],
)

catalog = ExerciseCatalog()


@router.get("")
def list_exercises():
    return catalog.all()


@router.get("/{exercise_id}")
def get_exercise(
    exercise_id: str,
):
    exercise = catalog.get(exercise_id)

    if exercise is None:
        raise HTTPException(
            404,
            "Exercise not found",
        )

    return exercise
