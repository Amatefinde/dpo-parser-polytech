from fastapi import APIRouter


from .courses import router as course_router
from src.settings import settings

router = APIRouter(prefix=settings.api_v1_prefix)
router.include_router(course_router)


__all__ = ["router"]
