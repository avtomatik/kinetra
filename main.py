from fastapi import FastAPI

from app.api.analytics import router as analytics_router
from app.api.exercises import router as exercises_router
from app.api.workouts import router as workouts_router

app = FastAPI(title="Kinetra")

app.include_router(workouts_router)

app.include_router(exercises_router)

app.include_router(analytics_router)
