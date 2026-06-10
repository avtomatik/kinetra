from app.services.import_legacy import convert_set


def test_convert_strength_set():

    result = convert_set(
        {
            "weight": 70,
            "reps": 5,
            "rest": 3,
        }
    )

    assert result == {
        "weight_kg": 70,
        "reps": 5,
        "rest_min": 3,
    }
