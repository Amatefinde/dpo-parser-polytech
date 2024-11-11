from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()


class ParserSettings(BaseSettings):
    domain: str = os.environ.get("DOMAIN")

    general_uri: str = f"https://{domain}/programs_dpo"
    course_url: str = f"https://{domain}"


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"

    parser_settings: ParserSettings = ParserSettings()


settings = Settings()
