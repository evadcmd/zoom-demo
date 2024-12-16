from pydantic_settings import BaseSettings


class Secret(BaseSettings):
    client_id: str
    client_secret: str
    redirect_uri: str


secret = Secret()
