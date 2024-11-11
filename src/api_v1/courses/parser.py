import httpx
from bs4 import BeautifulSoup

from .types import CourseCategory, Course


async def fetch(url: str) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

        if response.status_code == 200:
            return response.text
        else:
            print(f"Ошибка при загрузке страницы: {response.status_code}")


def parse_categories(html_content: str) -> list[CourseCategory]:
    course_categories = []
    if html_content:
        soup = BeautifulSoup(html_content, "html.parser")
        for elem in soup.find_all(class_=["t-item", "t-col", "t-col_12"]):
            if url_text := elem.find(string="Подробнее о блоке программ"):
                url = url_text.parent["href"]
                slug = url.split("/")[-1]
                course_category = CourseCategory(
                    url=url,
                    title=elem.find(class_=["t849__title", "t-name", "t-name_xl"]).text,
                    slug=slug,
                )
                course_categories.append(course_category)
    return course_categories


def _has_all_classes(tag):
    return all(cls in tag.get("class", []) for cls in ["t-col", "t-col_12", "t-align_center"])


def _parse_course(elem: BeautifulSoup) -> dict:
    title = elem.find(class_=["t581__title"]).text
    row_description = elem.find(class_=["t581__descr"])
    descriptions = row_description.get_text(separator="\n").split("\n")
    return {
        "title": title,
        "type": descriptions[0],
        "durations": descriptions[1],
        "format": descriptions[2],
        "cost": descriptions[3],
    }


def parse_courses(html_content: str):
    courses = []
    if html_content:
        soup = BeautifulSoup(html_content, "html.parser")
        for elem in soup.find_all(_has_all_classes):
            courses.append(Course.parse_obj(_parse_course(elem)))
    return courses
