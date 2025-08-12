from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATA_DIR: str = "data/uploads"
model_config = Settings.model_config if hasattr(Settings, 'model_config') else None
settings = Settings()