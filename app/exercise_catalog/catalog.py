import json
from pathlib import Path

from app.schemas.exercise import Exercise

CATALOG_FILE = Path(__file__).parent / "exercises.json"


class ExerciseCatalog:

    def __init__(self):

        self._items = {}

        data = json.loads(CATALOG_FILE.read_text())

        for item in data:

            exercise = Exercise(**item)

            self._items[exercise.id] = exercise

    def get(
        self,
        exercise_id: str,
    ) -> Exercise | None:

        return self._items.get(exercise_id)

    def find_by_alias(
        self,
        name: str,
    ) -> Exercise | None:

        lower = name.lower()

        for exercise in self._items.values():

            aliases = [a.lower() for a in exercise.aliases]

            if lower in aliases:
                return exercise

        return None

    def all(self):
        return list(self._items.values())
