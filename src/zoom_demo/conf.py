from pydantic_settings import BaseSettings


class Secret(BaseSettings):
    client_id: str
    client_secret: str
    redirect_url: str


secret = Secret()
