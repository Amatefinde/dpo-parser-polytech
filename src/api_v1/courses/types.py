from pydantic import BaseModel


class CourseCategory(BaseModel):
    title: str
    url: str
    slug: str


class Course(BaseModel):
    title: str
    type: str
    durations: str
    format: str
    cost: str
