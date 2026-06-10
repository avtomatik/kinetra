from pathlib import Path

from app.services.analytics_service import flatten_workout
from app.storage.parquet_store import ParquetStore


def export_workouts(
    workouts,
    output_file: Path,
):

    rows = []

    for workout in workouts:
        rows.extend(flatten_workout(workout))

    ParquetStore.write_rows(
        rows,
        output_file,
    )
