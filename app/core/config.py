from pydantic import BaseSettings

class Settings(BaseSettings):
    project_name: str = "Python API Boilerplate"
    debug: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
