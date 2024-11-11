from typing import Annotated, Iterable

from fastapi import APIRouter, Depends, UploadFile, Form, status, HTTPException

from . import CourseCategory
from ...settings import settings
from .parser import fetch, parse_categories, parse_courses


router = APIRouter(prefix="/courses", tags=["Courses"])


# @router.get("", response_model=ManyLiteratureEpubEntity)
# async def get_all_literature(
#     current_user: User = Depends(current_active_user_dependency),
#     db_session: AsyncSession = Depends(db_helper.session_dependency),
# ):
#     db_literature: Iterable[Literature] = await crud.get_all_user_literature(db_session, current_user)
#     f_id_and_id_map = {literature.f_literature_id: literature.id for literature in db_literature}
#     literature_entity = await literature_provider.get_many_book(list(f_id_and_id_map.keys()))
#     for literature in literature_entity.books:
#         literature.id = f_id_and_id_map[literature.id]
#     return literature_entity


@router.get("/categories", response_model=list[CourseCategory])
async def get_categories():
    html = await fetch(settings.parser_settings.general_uri)
    parsed_html = parse_categories(html)
    return parsed_html


@router.get("/course")
async def get_all_courses(slug: str):
    html = await fetch(f"{settings.parser_settings.course_url}/{slug}")
    parsed_html = parse_courses(html)
    return parsed_html
